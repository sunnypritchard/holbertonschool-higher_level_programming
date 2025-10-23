#!/usr/bin/env python3
"""
Task 3 Checker: Create force_name table with NOT NULL constraint
Tests for 3-force_name.sql
"""
import os
from tests.base_checker import TaskChecker


class Task3Checker(TaskChecker):
    """Checker for Task 3: Create force_name table with name NOT NULL"""

    def __init__(self, mysql_runner):
        super().__init__(3, "3-force_name.sql", mysql_runner)
        self.database = "hbtn_0d_2"
        self.table = "force_name"

    def setup(self) -> None:
        """Setup database and cleanup any existing table"""
        self.mysql.execute_sql_query(
            f"CREATE DATABASE IF NOT EXISTS {self.database};"
        )
        self.mysql.cleanup_table(self.table, self.database)

    def teardown(self) -> None:
        """Cleanup created table"""
        self.mysql.cleanup_table(self.table, self.database)

    def execute_tests(self) -> None:
        """Execute all tests for Task 3"""
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
        success, _, stderr = self.mysql.execute_sql_file(self.sql_file, self.database)

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

        # Test 3: Verify table was created
        table_exists = self.mysql.table_exists(self.table, self.database)
        self.add_test_result(
            "Table Creation",
            table_exists,
            f"Table '{self.table}' "
            f"{'was' if table_exists else 'was NOT'} created in "
            f"'{self.database}'"
        )

        if not table_exists:
            return

        # Test 4: Get and verify table structure
        success, structure = self.mysql.get_table_structure(
            self.table, self.database
        )

        if not success:
            self.add_test_result(
                "Get Table Structure",
                False,
                f"Failed to retrieve structure for table '{self.table}'"
            )
            return

        # Test 5: Verify 'id' column exists
        has_id = 'id' in structure
        self.add_test_result(
            "Column 'id' Exists",
            has_id,
            f"Column 'id' {'exists' if has_id else 'does NOT exist'}"
        )

        # Test 6: Verify 'name' column exists and is NOT NULL
        has_name = 'name' in structure
        self.add_test_result(
            "Column 'name' Exists",
            has_name,
            f"Column 'name' {'exists' if has_name else 'does NOT exist'}"
        )

        if has_name:
            name_not_null = structure['name']['null'] == 'NO'
            self.add_test_result(
                "Column 'name' is NOT NULL",
                name_not_null,
                f"Column 'name' {'is' if name_not_null else 'is NOT'} "
                "constrained as NOT NULL (forces name)",
                f"Actual: {structure['name']['null']}" if not name_not_null else None
            )

            # Test 7: Verify 'name' is VARCHAR(256)
            name_type = structure['name']['type']
            correct_type = 'varchar(256)' in name_type.lower()
            self.add_test_result(
                "Column 'name' Type is VARCHAR(256)",
                correct_type,
                f"Column 'name' type "
                f"{'is' if correct_type else 'is NOT'} VARCHAR(256)",
                f"Actual: {name_type}" if not correct_type else None
            )

        # Test 8: Test that inserting NULL name fails
        insert_null = f"INSERT INTO {self.database}.{self.table} (id) VALUES (1);"
        success_null, _, _ = self.mysql.execute_sql_query(insert_null)
        self.add_test_result(
            "NOT NULL Constraint Works (INSERT with NULL name fails)",
            not success_null,
            f"Inserting NULL name "
            f"{'correctly fails' if not success_null else 'INCORRECTLY succeeds'}"
        )

        # Clean up test data
        self.mysql.execute_sql_query(
            f"DELETE FROM {self.database}.{self.table};"
        )

        # Test 9: Test idempotency
        success2, _, stderr2 = self.mysql.execute_sql_file(self.sql_file, self.database)
        self.add_test_result(
            "Idempotency Test",
            success2,
            f"Script {'can' if success2 else 'CANNOT'} be run multiple times "
            "without errors",
            stderr2 if not success2 else None
        )
