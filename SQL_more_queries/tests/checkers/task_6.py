#!/usr/bin/env python3
"""
Task 6 Checker: Create states table with AUTO_INCREMENT PRIMARY KEY
Tests for 6-states.sql
"""
import os
from tests.base_checker import TaskChecker


class Task6Checker(TaskChecker):
    """Checker for Task 6: Create states table with AUTO_INCREMENT PRIMARY KEY"""

    def __init__(self, mysql_runner):
        super().__init__(6, "6-states.sql", mysql_runner)
        self.database = "hbtn_0d_usa"
        self.table = "states"

    def setup(self) -> None:
        """Setup database and cleanup any existing table"""
        self.mysql.execute_sql_query(
            f"CREATE DATABASE IF NOT EXISTS {self.database};"
        )
        self.mysql.cleanup_table(self.table, self.database)

    def teardown(self) -> None:
        """Cleanup created table and database"""
        self.mysql.cleanup_table(self.table, self.database)
        self.mysql.cleanup_database(self.database)

    def execute_tests(self) -> None:
        """Execute all tests for Task 6"""
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

        # Test 5: Verify 'id' column exists and is PRIMARY KEY
        has_id = 'id' in structure
        self.add_test_result(
            "Column 'id' Exists",
            has_id,
            f"Column 'id' {'exists' if has_id else 'does NOT exist'}"
        )

        if has_id:
            # Check PRIMARY KEY
            key_type = structure['id']['key']
            is_primary = key_type == 'PRI'
            self.add_test_result(
                "Column 'id' is PRIMARY KEY",
                is_primary,
                f"Column 'id' {'is' if is_primary else 'is NOT'} PRIMARY KEY",
                f"Actual key type: {key_type}" if not is_primary else None
            )

            # Check AUTO_INCREMENT
            extra = structure['id']['extra']
            is_auto_increment = extra and 'auto_increment' in extra.lower()
            self.add_test_result(
                "Column 'id' has AUTO_INCREMENT",
                is_auto_increment,
                f"Column 'id' "
                f"{'has' if is_auto_increment else 'does NOT have'} "
                "AUTO_INCREMENT",
                f"Actual extra: {extra}" if not is_auto_increment else None
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
                "constrained as NOT NULL",
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

        # Test 8: Test AUTO_INCREMENT - insert records and verify ids
        insert1 = f"INSERT INTO {self.database}.{self.table} (name) VALUES ('California');"
        success1, _, _ = self.mysql.execute_sql_query(insert1)

        if success1:
            insert2 = f"INSERT INTO {self.database}.{self.table} (name) VALUES ('Arizona');"
            success2, _, _ = self.mysql.execute_sql_query(insert2)

            if success2:
                # Verify auto-increment worked
                select_query = f"SELECT id FROM {self.database}.{self.table} ORDER BY id;"
                success_select, stdout, _ = self.mysql.execute_sql_query(select_query)
                if success_select:
                    # Should have sequential ids (1, 2)
                    has_auto_inc = '1' in stdout and '2' in stdout
                    self.add_test_result(
                        "AUTO_INCREMENT Works (generates sequential ids)",
                        has_auto_inc,
                        f"AUTO_INCREMENT "
                        f"{'works correctly' if has_auto_inc else 'does NOT work'}",
                        stdout if not has_auto_inc else None
                    )
                else:
                    self.add_test_result(
                        "AUTO_INCREMENT Test",
                        False,
                        "Failed to verify AUTO_INCREMENT"
                    )
            else:
                self.add_test_result(
                    "Insert Test",
                    False,
                    "Failed to insert second test record"
                )
        else:
            self.add_test_result(
                "Insert Test",
                False,
                "Failed to insert first test record"
            )

        # Test 9: Test that inserting NULL name fails
        insert_null = f"INSERT INTO {self.database}.{self.table} (id) VALUES (100);"
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

        # Test 10: Test idempotency
        success3, _, stderr3 = self.mysql.execute_sql_file(self.sql_file)
        self.add_test_result(
            "Idempotency Test",
            success3,
            f"Script {'can' if success3 else 'CANNOT'} be run multiple times "
            "without errors",
            stderr3 if not success3 else None
        )
