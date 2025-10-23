#!/usr/bin/env python3
"""
Task 1 Checker: Create user with all privileges
Tests for 1-create_user.sql
"""
import os
from tests.base_checker import TaskChecker


class Task1Checker(TaskChecker):
    """Checker for Task 1: Create user_0d_1 with ALL PRIVILEGES"""

    def __init__(self, mysql_runner):
        super().__init__(1, "1-create_user.sql", mysql_runner)
        self.username = "user_0d_1"
        self.host = "localhost"

    def setup(self) -> None:
        """Cleanup any existing user before test"""
        self.mysql.cleanup_user(self.username, self.host)

    def teardown(self) -> None:
        """Cleanup created user after test"""
        self.mysql.cleanup_user(self.username, self.host)

    def execute_tests(self) -> None:
        """Execute all tests for Task 1"""
        # Test 1: File existence
        if not os.path.exists(self.sql_file):
            self.add_test_result(
                "File Existence",
                False,
                f"SQL file '{self.sql_file}' not found"
            )
            return

        self.add_test_result(
            "File Existence",
            True,
            f"SQL file '{self.sql_file}' exists"
        )

        # Test 2: Execute SQL file
        success, _, stderr = self.mysql.execute_sql_file(self.sql_file)

        if not success:
            self.add_test_result(
                "SQL Execution",
                False,
                "Failed to execute SQL file",
                stderr
            )
            return

        self.add_test_result(
            "SQL Execution",
            True,
            "SQL file executed successfully"
        )

        # Test 3: Verify user was created
        user_exists = self.mysql.user_exists(self.username, self.host)
        self.add_test_result(
            "User Creation",
            user_exists,
            f"User '{self.username}'@'{self.host}' "
            f"{'was' if user_exists else 'was NOT'} created"
        )

        if not user_exists:
            return

        # Test 4: Verify user has ALL PRIVILEGES
        success, grants = self.mysql.get_user_grants(self.username, self.host)

        if not success:
            self.add_test_result(
                "Get User Grants",
                False,
                f"Failed to retrieve grants for '{self.username}'@'{self.host}'"
            )
            return

        # Check for ALL PRIVILEGES (can be granted as individual privileges)
        has_all_privileges = any(
            "ALL PRIVILEGES" in grant.upper() or "GRANT ALL" in grant.upper()
            for grant in grants
        )

        # If not explicitly "ALL PRIVILEGES", check if user has comprehensive privileges
        if not has_all_privileges:
            # Check for key privileges that indicate admin access
            key_privs = ["SELECT", "INSERT", "UPDATE", "DELETE", "CREATE",
                        "DROP", "ALTER", "INDEX"]
            has_key_privs = all(
                any(priv in grant.upper() for grant in grants)
                for priv in key_privs
            )
            has_all_privileges = has_key_privs

        self.add_test_result(
            "ALL PRIVILEGES Granted",
            has_all_privileges,
            f"User {'has' if has_all_privileges else 'does NOT have'} "
            "ALL PRIVILEGES (or equivalent comprehensive privileges)",
            "\n".join(grants) if not has_all_privileges else None
        )

        # Test 5: Verify script uses IF NOT EXISTS
        with open(self.sql_file, 'r') as f:
            content = f.read().upper()

        has_if_not_exists = "IF NOT EXISTS" in content
        self.add_test_result(
            "Uses IF NOT EXISTS",
            has_if_not_exists,
            f"Script {'uses' if has_if_not_exists else 'does NOT use'} "
            "IF NOT EXISTS"
        )

        # Test 6: Test idempotency - run script twice
        success2, _, stderr2 = self.mysql.execute_sql_file(self.sql_file)
        self.add_test_result(
            "Idempotency Test",
            success2,
            f"Script {'can' if success2 else 'CANNOT'} be run multiple times "
            "without errors",
            stderr2 if not success2 else None
        )
