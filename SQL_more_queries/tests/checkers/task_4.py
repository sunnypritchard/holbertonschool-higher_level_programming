#!/usr/bin/env python3
"""
Task 4 Checker: Create id_not_null table with DEFAULT value
Tests for 4-never_empty.sql
"""
import os
from tests.base_checker import TaskChecker


class Task4Checker(TaskChecker):
    """Checker for Task 4: Create id_not_null table with id DEFAULT 1"""

    def __init__(self, mysql_runner):
        super().__init__(4, "4-never_empty.sql", mysql_runner)
        self.database = "hbtn_0d_2"
        self.table = "id_not_null"

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
        """Execute all tests for Task 4"""
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

        # Test 5: Verify 'id' column exists with DEFAULT 1
        has_id = 'id' in structure
        self.add_test_result(
            "Column 'id' Exists",
            has_id,
            f"Column 'id' {'exists' if has_id else 'does NOT exist'}"
        )

        if has_id:
            default_value = structure['id']['default']
            has_default_1 = default_value == '1'
            self.add_test_result(
                "Column 'id' DEFAULT Value is 1",
                has_default_1,
                f"Column 'id' default "
                f"{'is' if has_default_1 else 'is NOT'} 1 (never empty)",
                f"Actual: {default_value}" if not has_default_1 else None
            )

        # Test 6: Verify 'name' column exists
        has_name = 'name' in structure
        self.add_test_result(
            "Column 'name' Exists",
            has_name,
            f"Column 'name' {'exists' if has_name else 'does NOT exist'}"
        )

        if has_name:
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

        # Test 8: Test that inserting without id uses default value
        insert_query = f"INSERT INTO {self.database}.{self.table} (name) VALUES ('test');"
        success_insert, _, _ = self.mysql.execute_sql_query(insert_query)

        if success_insert:
            # Check that the id is 1
            select_query = f"SELECT id FROM {self.database}.{self.table} WHERE name = 'test';"
            success_select, stdout, _ = self.mysql.execute_sql_query(select_query)
            if success_select:
                has_default = '1' in stdout
                self.add_test_result(
                    "DEFAULT Value Works (id=1 when not specified)",
                    has_default,
                    f"Default value "
                    f"{'works correctly' if has_default else 'does NOT work'}",
                    stdout if not has_default else None
                )
            else:
                self.add_test_result(
                    "DEFAULT Value Works",
                    False,
                    "Failed to verify default value"
                )
        else:
            self.add_test_result(
                "Insert Test",
                False,
                "Failed to insert test data"
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
