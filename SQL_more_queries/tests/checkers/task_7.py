#!/usr/bin/env python3
"""
Task Checker for Task 7
- Task 7: Create database and cities table with FOREIGN KEY constraint
"""
import os
from tests.base_checker import TaskChecker


class Task7Checker(TaskChecker):
    """Checker for Task 7: Create cities table with FOREIGN KEY to states"""

    def __init__(self, mysql_runner):
        super().__init__(7, "7-cities.sql", mysql_runner)
        self.database = "hbtn_0d_usa"
        self.states_table = "states"
        self.cities_table = "cities"

    def setup(self) -> None:
        """Setup: Create database and ensure clean state"""
        # Create database if needed
        self.mysql.execute_sql_query(f"CREATE DATABASE IF NOT EXISTS {self.database};")
        # Clean up tables (cities first due to FK constraint)
        self.mysql.cleanup_table(self.cities_table, self.database)
        self.mysql.cleanup_table(self.states_table, self.database)
        # Create states table (required for FK)
        create_states = f"""
        CREATE TABLE IF NOT EXISTS {self.database}.{self.states_table} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(256) NOT NULL
        );
        """
        self.mysql.execute_sql_query(create_states)

    def teardown(self) -> None:
        """Cleanup: Remove tables and database"""
        self.mysql.cleanup_table(self.cities_table, self.database)
        self.mysql.cleanup_table(self.states_table, self.database)
        self.mysql.cleanup_database(self.database)

    def execute_tests(self) -> None:
        """Execute tests for Task 7"""
        # Test 1: Check if SQL file exists
        if not os.path.exists(self.sql_file):
            self.add_test_result(
                "File Existence",
                False,
                f"SQL file '{self.sql_file}' not found"
            )
            return
        else:
            self.add_test_result(
                "File Existence",
                True,
                f"SQL file '{self.sql_file}' exists"
            )

        # Test 2: Execute the SQL file
        success, _, stderr = self.mysql.execute_sql_file(self.sql_file)

        if not success:
            self.add_test_result(
                "SQL Execution",
                False,
                "Failed to execute SQL file",
                stderr
            )
            return
        else:
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
            f"Database '{self.database}' {'was' if db_exists else 'was NOT'} created"
        )

        if not db_exists:
            return

        # Test 4: Verify cities table was created
        table_exists = self.mysql.table_exists(self.cities_table, self.database)
        self.add_test_result(
            "Table Creation",
            table_exists,
            f"Table '{self.cities_table}' {'was' if table_exists else 'was NOT'} created in '{self.database}'"
        )

        if not table_exists:
            return

        # Test 5: Get and verify table structure
        success, structure = self.mysql.get_table_structure(self.cities_table, self.database)

        if not success:
            self.add_test_result(
                "Get Table Structure",
                False,
                f"Failed to retrieve structure for table '{self.cities_table}'"
            )
            return

        # Test 6: Verify 'id' column exists
        has_id = 'id' in structure
        self.add_test_result(
            "Column 'id' Exists",
            has_id,
            f"Column 'id' {'exists' if has_id else 'does NOT exist'}"
        )

        if has_id:
            # Test 7: Verify 'id' is PRIMARY KEY
            key_type = structure['id']['key']
            is_primary = key_type == 'PRI'
            self.add_test_result(
                "Column 'id' is PRIMARY KEY",
                is_primary,
                f"Column 'id' {'is' if is_primary else 'is NOT'} PRIMARY KEY",
                f"Actual key type: {key_type}" if not is_primary else None
            )

            # Test 8: Verify 'id' has AUTO_INCREMENT
            extra = structure['id']['extra']
            is_auto_increment = extra and 'auto_increment' in extra.lower()
            self.add_test_result(
                "Column 'id' has AUTO_INCREMENT",
                is_auto_increment,
                f"Column 'id' {'has' if is_auto_increment else 'does NOT have'} AUTO_INCREMENT",
                f"Actual extra: {extra}" if not is_auto_increment else None
            )

            # Test 9: Verify 'id' is NOT NULL
            id_not_null = structure['id']['null'] == 'NO'
            self.add_test_result(
                "Column 'id' is NOT NULL",
                id_not_null,
                f"Column 'id' {'is' if id_not_null else 'is NOT'} NOT NULL",
                f"Actual: {structure['id']['null']}" if not id_not_null else None
            )

        # Test 10: Verify 'state_id' column exists
        has_state_id = 'state_id' in structure
        self.add_test_result(
            "Column 'state_id' Exists",
            has_state_id,
            f"Column 'state_id' {'exists' if has_state_id else 'does NOT exist'}"
        )

        if has_state_id:
            # Test 11: Verify 'state_id' is NOT NULL
            state_id_not_null = structure['state_id']['null'] == 'NO'
            self.add_test_result(
                "Column 'state_id' is NOT NULL",
                state_id_not_null,
                f"Column 'state_id' {'is' if state_id_not_null else 'is NOT'} NOT NULL",
                f"Actual: {structure['state_id']['null']}" if not state_id_not_null else None
            )

            # Test 12: Verify 'state_id' is INT type
            state_id_type = structure['state_id']['type']
            is_int = 'int' in state_id_type.lower()
            self.add_test_result(
                "Column 'state_id' Type is INT",
                is_int,
                f"Column 'state_id' type {'is' if is_int else 'is NOT'} INT",
                f"Actual: {state_id_type}" if not is_int else None
            )

        # Test 13: Verify 'name' column exists
        has_name = 'name' in structure
        self.add_test_result(
            "Column 'name' Exists",
            has_name,
            f"Column 'name' {'exists' if has_name else 'does NOT exist'}"
        )

        if has_name:
            # Test 14: Verify 'name' is NOT NULL
            name_not_null = structure['name']['null'] == 'NO'
            self.add_test_result(
                "Column 'name' is NOT NULL",
                name_not_null,
                f"Column 'name' {'is' if name_not_null else 'is NOT'} constrained as NOT NULL",
                f"Actual: {structure['name']['null']}" if not name_not_null else None
            )

            # Test 15: Verify 'name' is VARCHAR(256)
            name_type = structure['name']['type']
            correct_type = 'varchar(256)' in name_type.lower()
            self.add_test_result(
                "Column 'name' Type is VARCHAR(256)",
                correct_type,
                f"Column 'name' type {'is' if correct_type else 'is NOT'} VARCHAR(256)",
                f"Actual: {name_type}" if not correct_type else None
            )

        # Test 16: Verify FOREIGN KEY constraint exists
        # Query to check for foreign key
        fk_query = f"""
        SELECT
            CONSTRAINT_NAME,
            REFERENCED_TABLE_NAME,
            REFERENCED_COLUMN_NAME
        FROM
            INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        WHERE
            TABLE_SCHEMA = '{self.database}'
            AND TABLE_NAME = '{self.cities_table}'
            AND REFERENCED_TABLE_NAME IS NOT NULL;
        """
        success_fk, fk_output, _ = self.mysql.execute_sql_query(fk_query)

        if success_fk and fk_output:
            has_fk = self.states_table in fk_output
            references_id = 'id' in fk_output
            self.add_test_result(
                "FOREIGN KEY Constraint Exists",
                has_fk and references_id,
                f"FOREIGN KEY {'exists' if has_fk else 'does NOT exist'} referencing '{self.states_table}.id'",
                fk_output if not (has_fk and references_id) else None
            )
        else:
            self.add_test_result(
                "FOREIGN KEY Constraint Check",
                False,
                "Failed to check FOREIGN KEY constraint"
            )

        # Test 17: Test FOREIGN KEY constraint functionality
        # Insert a state first
        insert_state = f"INSERT INTO {self.database}.{self.states_table} (name) VALUES ('California');"
        success_state, _, _ = self.mysql.execute_sql_query(insert_state)

        if success_state:
            # Try to insert a city with valid state_id
            insert_city_valid = f"INSERT INTO {self.database}.{self.cities_table} (state_id, name) VALUES (1, 'San Francisco');"
            success_valid, _, _ = self.mysql.execute_sql_query(insert_city_valid)

            self.add_test_result(
                "FOREIGN KEY Allows Valid Reference",
                success_valid,
                f"Inserting city with valid state_id {'succeeds' if success_valid else 'FAILS'}"
            )

            # Try to insert a city with invalid state_id (should fail)
            insert_city_invalid = f"INSERT INTO {self.database}.{self.cities_table} (state_id, name) VALUES (999, 'Invalid City');"
            success_invalid, _, _ = self.mysql.execute_sql_query(insert_city_invalid)

            self.add_test_result(
                "FOREIGN KEY Rejects Invalid Reference",
                not success_invalid,
                f"Inserting city with invalid state_id {'correctly fails' if not success_invalid else 'INCORRECTLY succeeds'}"
            )
        else:
            self.add_test_result(
                "FOREIGN KEY Functionality Test",
                False,
                "Failed to insert test state for FK testing"
            )

        # Clean up test data
        self.mysql.execute_sql_query(f"DELETE FROM {self.database}.{self.cities_table};")
        self.mysql.execute_sql_query(f"DELETE FROM {self.database}.{self.states_table};")

        # Test 18: Test AUTO_INCREMENT functionality
        insert1 = f"INSERT INTO {self.database}.{self.states_table} (name) VALUES ('Texas');"
        self.mysql.execute_sql_query(insert1)

        # Get the actual state_id that was just inserted
        get_state_id = f"SELECT id FROM {self.database}.{self.states_table} WHERE name='Texas' LIMIT 1;"
        success_get_id, state_id_output, _ = self.mysql.execute_sql_query(get_state_id)

        if not success_get_id or not state_id_output:
            self.add_test_result(
                "Get State ID",
                False,
                "Failed to retrieve inserted state ID"
            )
            return

        # Extract the numeric ID from the output
        try:
            state_id = int(state_id_output.strip().split('\n')[-1])
        except (ValueError, IndexError):
            self.add_test_result(
                "Parse State ID",
                False,
                f"Failed to parse state ID from output: {state_id_output}"
            )
            return

        insert_city1 = f"INSERT INTO {self.database}.{self.cities_table} (state_id, name) VALUES ({state_id}, 'Houston');"
        success1, _, _ = self.mysql.execute_sql_query(insert_city1)

        if success1:
            insert_city2 = f"INSERT INTO {self.database}.{self.cities_table} (state_id, name) VALUES ({state_id}, 'Dallas');"
            success2, _, _ = self.mysql.execute_sql_query(insert_city2)

            if success2:
                # Verify auto-increment worked
                select_query = f"SELECT id FROM {self.database}.{self.cities_table} ORDER BY id;"
                success_select, stdout, _ = self.mysql.execute_sql_query(select_query)
                if success_select:
                    # Extract the IDs from the output
                    try:
                        lines = stdout.strip().split('\n')
                        # Skip header line if present
                        ids = [int(line.strip()) for line in lines if line.strip().isdigit()]
                        # Check if we have exactly 2 IDs and they are consecutive
                        has_auto_inc = len(ids) == 2 and ids[1] == ids[0] + 1
                    except (ValueError, IndexError):
                        has_auto_inc = False

                    self.add_test_result(
                        "AUTO_INCREMENT Works (generates sequential ids)",
                        has_auto_inc,
                        f"AUTO_INCREMENT {'works correctly' if has_auto_inc else 'does NOT work'}",
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

        # Clean up again
        self.mysql.execute_sql_query(f"DELETE FROM {self.database}.{self.cities_table};")
        self.mysql.execute_sql_query(f"DELETE FROM {self.database}.{self.states_table};")

        # Test 19: Verify script uses IF NOT EXISTS for database
        with open(self.sql_file, 'r') as f:
            content = f.read().upper()

        has_db_if_not_exists = "CREATE DATABASE IF NOT EXISTS" in content
        self.add_test_result(
            "Uses IF NOT EXISTS for Database",
            has_db_if_not_exists,
            f"Script {'uses' if has_db_if_not_exists else 'does NOT use'} IF NOT EXISTS for database creation"
        )

        # Test 20: Verify script uses IF NOT EXISTS for table
        has_table_if_not_exists = "CREATE TABLE IF NOT EXISTS" in content
        self.add_test_result(
            "Uses IF NOT EXISTS for Table",
            has_table_if_not_exists,
            f"Script {'uses' if has_table_if_not_exists else 'does NOT use'} IF NOT EXISTS for table creation"
        )

        # Test 21: Test idempotency - run script twice
        success2, _, stderr2 = self.mysql.execute_sql_file(self.sql_file)
        self.add_test_result(
            "Idempotency Test",
            success2,
            f"Script {'can' if success2 else 'CANNOT'} be run multiple times without errors",
            stderr2 if not success2 else None
        )
