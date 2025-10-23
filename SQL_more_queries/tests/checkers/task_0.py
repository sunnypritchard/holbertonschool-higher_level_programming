#!/usr/bin/env python3
"""
Task 0 Checker: List privileges
Tests for 0-privileges.sql
"""
import os
from tests.base_checker import TaskChecker


class Task0Checker(TaskChecker):
    """Checker for Task 0: List privileges for user_0d_1 and user_0d_2"""

    def __init__(self, mysql_runner):
        super().__init__(0, "0-privileges.sql", mysql_runner)
        self.test_users = [
            ("user_0d_1", "localhost"),
            ("user_0d_2", "localhost")
        ]

    def setup(self) -> None:
        """Setup test users for privilege checking"""
        # Create user_0d_1 with ALL PRIVILEGES
        self.mysql.cleanup_user("user_0d_1")
        self.mysql.execute_sql_query(
            "CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pass';"
        )
        self.mysql.execute_sql_query(
            "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';"
        )

        # Create user_0d_2 with limited privileges
        self.mysql.cleanup_user("user_0d_2")
        self.mysql.execute_sql_query(
            "CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pass';"
        )
        self.mysql.execute_sql_query(
            "GRANT SELECT, INSERT ON *.* TO 'user_0d_2'@'localhost';"
        )

        self.mysql.execute_sql_query("FLUSH PRIVILEGES;")

    def teardown(self) -> None:
        """Cleanup test users"""
        for username, host in self.test_users:
            self.mysql.cleanup_user(username, host)

    def execute_tests(self) -> None:
        """Execute all tests for Task 0"""
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
        success, stdout, stderr = self.mysql.execute_sql_file(self.sql_file)

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

        # Test 3: Verify user grants are displayed in output
        for username, host in self.test_users:
            user_in_output = username in stdout
            self.add_test_result(
                f"User Grants Display ({username})",
                user_in_output,
                f"Grants for '{username}'@'{host}' "
                f"{'are' if user_in_output else 'are NOT'} displayed",
                stdout if not user_in_output else None
            )

        # Test 4: Verify script uses SHOW GRANTS command
        with open(self.sql_file, 'r') as f:
            content = f.read().upper()

        has_show_grants = "SHOW GRANTS" in content
        self.add_test_result(
            "Uses SHOW GRANTS Command",
            has_show_grants,
            f"Script {'uses' if has_show_grants else 'does NOT use'} "
            "SHOW GRANTS command"
        )

        # Test 5: Verify both users are referenced in the script
        with open(self.sql_file, 'r') as f:
            content = f.read()

        for username, host in self.test_users:
            user_referenced = username in content
            self.add_test_result(
                f"User Reference ({username})",
                user_referenced,
                f"User '{username}' "
                f"{'is' if user_referenced else 'is NOT'} referenced "
                "in the script"
            )
