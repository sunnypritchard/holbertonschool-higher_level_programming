#!/usr/bin/env python3
"""
Task 5 Checker: Create unique_id table with UNIQUE constraint
Tests for 5-unique_id.sql
"""
import os
from tests.base_checker import TaskChecker


class Task5Checker(TaskChecker):
    """Checker for Task 5: Create unique_id table with UNIQUE id"""

    def __init__(self, mysql_runner):
        super().__init__(5, "5-unique_id.sql", mysql_runner)
        self.database = "hbtn_0d_2"
        self.table = "unique_id"

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
        """Execute all tests for Task 5"""
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

        # Test 5: Verify 'id' column exists with DEFAULT 1 and UNIQUE
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
                f"{'is' if has_default_1 else 'is NOT'} 1",
                f"Actual: {default_value}" if not has_default_1 else None
            )

            # Check UNIQUE constraint
            key_type = structure['id']['key']
            is_unique = key_type in ['UNI', 'PRI']
            self.add_test_result(
                "Column 'id' has UNIQUE Constraint",
                is_unique,
                f"Column 'id' "
                f"{'has' if is_unique else 'does NOT have'} UNIQUE constraint",
                f"Actual key type: {key_type}" if not is_unique else None
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

        # Test 8: Test UNIQUE constraint - insert same id twice should fail
        insert_query1 = f"INSERT INTO {self.database}.{self.table} (id, name) VALUES (1, 'test1');"
        success1, _, _ = self.mysql.execute_sql_query(insert_query1)

        if success1:
            insert_query2 = f"INSERT INTO {self.database}.{self.table} (id, name) VALUES (1, 'test2');"
            success2, _, _ = self.mysql.execute_sql_query(insert_query2)
            self.add_test_result(
                "UNIQUE Constraint Works (duplicate id fails)",
                not success2,
                f"Inserting duplicate id "
                f"{'correctly fails' if not success2 else 'INCORRECTLY succeeds'}"
            )
        else:
            self.add_test_result(
                "Insert Test",
                False,
                "Failed to insert initial test data"
            )

        # Clean up test data
        self.mysql.execute_sql_query(
            f"DELETE FROM {self.database}.{self.table};"
        )

        # Test 9: Test idempotency
        success3, _, stderr3 = self.mysql.execute_sql_file(self.sql_file, self.database)
        self.add_test_result(
            "Idempotency Test",
            success3,
            f"Script {'can' if success3 else 'CANNOT'} be run multiple times "
            "without errors",
            stderr3 if not success3 else None
        )
