#!/usr/bin/env python3
"""
Task 2 Checker: Create database and user with SELECT privilege
Tests for 2-create_read_user.sql
"""
import os
from tests.base_checker import TaskChecker


class Task2Checker(TaskChecker):
    """Checker for Task 2: Create hbtn_0d_2 database and user_0d_2 with SELECT privilege"""

    def __init__(self, mysql_runner):
        super().__init__(2, "2-create_read_user.sql", mysql_runner)
        self.database = "hbtn_0d_2"
        self.username = "user_0d_2"
        self.host = "localhost"

    def setup(self) -> None:
        """Cleanup any existing database and user"""
        self.mysql.cleanup_user(self.username, self.host)
        self.mysql.cleanup_database(self.database)

    def teardown(self) -> None:
        """Cleanup created database and user"""
        self.mysql.cleanup_user(self.username, self.host)
        self.mysql.cleanup_database(self.database)

    def execute_tests(self) -> None:
        """Execute all tests for Task 2"""
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

        # Test 3: Verify database was created
        db_exists = self.mysql.database_exists(self.database)
        self.add_test_result(
            "Database Creation",
            db_exists,
            f"Database '{self.database}' "
            f"{'was' if db_exists else 'was NOT'} created"
        )

        # Test 4: Verify user was created
        user_exists = self.mysql.user_exists(self.username, self.host)
        self.add_test_result(
            "User Creation",
            user_exists,
            f"User '{self.username}'@'{self.host}' "
            f"{'was' if user_exists else 'was NOT'} created"
        )

        if not user_exists:
            return

        # Test 5: Verify user has SELECT privilege on the database
        success, grants = self.mysql.get_user_grants(self.username, self.host)

        if not success:
            self.add_test_result(
                "Get User Grants",
                False,
                f"Failed to retrieve grants for '{self.username}'@'{self.host}'"
            )
            return

        has_select = any(
            "SELECT" in grant.upper() and self.database in grant
            for grant in grants
        )
        self.add_test_result(
            "SELECT Privilege on Database",
            has_select,
            f"User {'has' if has_select else 'does NOT have'} SELECT "
            f"privilege on '{self.database}'",
            "\n".join(grants) if not has_select else None
        )

        # Test 6: Verify user does NOT have other privileges
        dangerous_privs = ["INSERT", "UPDATE", "DELETE", "DROP", "CREATE",
                          "ALL PRIVILEGES"]
        has_only_select = not any(
            any(priv in grant.upper() for priv in dangerous_privs)
            for grant in grants
        )
        self.add_test_result(
            "Limited Privileges (Only SELECT)",
            has_only_select,
            f"User {'has only SELECT' if has_only_select else 'has MORE than SELECT'} privilege",
            "\n".join(grants) if not has_only_select else None
        )

        # Test 7: Verify script uses IF NOT EXISTS
        with open(self.sql_file, 'r') as f:
            content = f.read().upper()

        if_not_exists_count = content.count("IF NOT EXISTS")
        has_enough_if_not_exists = if_not_exists_count >= 2
        self.add_test_result(
            "Uses IF NOT EXISTS (database and user)",
            has_enough_if_not_exists,
            f"Script uses IF NOT EXISTS {if_not_exists_count} time(s) "
            "(expected at least 2)"
        )

        # Test 8: Test idempotency
        success2, _, stderr2 = self.mysql.execute_sql_file(self.sql_file)
        self.add_test_result(
            "Idempotency Test",
            success2,
            f"Script {'can' if success2 else 'CANNOT'} be run multiple times "
            "without errors",
            stderr2 if not success2 else None
        )
