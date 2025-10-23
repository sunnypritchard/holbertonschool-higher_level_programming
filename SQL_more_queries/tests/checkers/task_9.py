#!/usr/bin/env python3
"""
Task 9 Checker: List cities with state names using JOIN
Tests for 9-cities_by_state_join.sql
"""
import os
from tests.base_checker import TaskChecker


class Task9Checker(TaskChecker):
    """Checker for Task 9: List all cities with state names using JOIN"""

    def __init__(self, mysql_runner):
        super().__init__(
            9,
            "9-cities_by_state_join.sql",
            mysql_runner
        )
        self.database = "hbtn_0d_usa"
        self.states_table = "states"
        self.cities_table = "cities"

    def setup(self) -> None:
        """Setup: Create database and tables with test data"""
        # Create database
        self.mysql.execute_sql_query(
            f"CREATE DATABASE IF NOT EXISTS {self.database};"
        )

        # Clean up tables (cities first due to FK constraint)
        self.mysql.cleanup_table(self.cities_table, self.database)
        self.mysql.cleanup_table(self.states_table, self.database)

        # Create states table
        create_states = f"""
        CREATE TABLE IF NOT EXISTS {self.database}.{self.states_table} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(256) NOT NULL
        );
        """
        self.mysql.execute_sql_query(create_states)

        # Create cities table
        create_cities = f"""
        CREATE TABLE IF NOT EXISTS {self.database}.{self.cities_table} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            state_id INT NOT NULL,
            name VARCHAR(256) NOT NULL,
            FOREIGN KEY (state_id) REFERENCES {self.database}.{self.states_table}(id)
        );
        """
        self.mysql.execute_sql_query(create_cities)

        # Insert test states
        self.mysql.execute_sql_query(
            f"INSERT INTO {self.database}.{self.states_table} (name) VALUES "
            "('California'), ('Arizona'), ('Texas'), ('New York');"
        )

        # Insert test cities with known IDs
        self.mysql.execute_sql_query(
            f"INSERT INTO {self.database}.{self.cities_table} "
            "(state_id, name) VALUES "
            "(1, 'San Francisco'), "
            "(1, 'San Jose'), "
            "(2, 'Phoenix'), "
            "(1, 'Los Angeles'), "
            "(3, 'Houston'), "
            "(3, 'Dallas'), "
            "(4, 'New York City'), "
            "(2, 'Tucson');"
        )

    def teardown(self) -> None:
        """Cleanup: Remove tables and database"""
        self.mysql.cleanup_table(self.cities_table, self.database)
        self.mysql.cleanup_table(self.states_table, self.database)
        self.mysql.cleanup_database(self.database)

    def execute_tests(self) -> None:
        """Execute all tests for Task 9"""
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

        # Test 2: Verify script uses only ONE SELECT statement
        with open(self.sql_file, 'r') as f:
            content = f.read()

        # Remove comments before checking
        lines = content.split('\n')
        sql_lines = [line.split('--')[0] for line in lines]
        sql_code = '\n'.join(sql_lines).upper()

        select_count = sql_code.count('SELECT')
        uses_one_select = select_count == 1

        self.add_test_result(
            "Uses Only One SELECT Statement",
            uses_one_select,
            f"Script uses {select_count} SELECT statement(s) "
            f"(expected 1)",
            "Must use only one SELECT statement" if not uses_one_select else None
        )

        # Test 3: Verify script uses JOIN keyword
        has_join = 'JOIN' in sql_code
        self.add_test_result(
            "Uses JOIN Keyword",
            has_join,
            f"Script {'uses' if has_join else 'does NOT use'} JOIN keyword",
            "Script must use JOIN to combine tables" if not has_join else None
        )

        # Test 4: Execute SQL file with database parameter
        success, stdout, stderr = self.mysql.execute_sql_file(
            self.sql_file,
            self.database
        )

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

        # Test 5: Verify output contains all expected cities
        expected_cities = [
            'San Francisco',
            'San Jose',
            'Phoenix',
            'Los Angeles',
            'Houston',
            'Dallas',
            'New York City',
            'Tucson'
        ]

        all_cities_found = True
        missing_cities = []
        for city in expected_cities:
            if city not in stdout:
                all_cities_found = False
                missing_cities.append(city)

        self.add_test_result(
            "All Cities Listed",
            all_cities_found,
            f"All {len(expected_cities)} cities "
            f"{'are' if all_cities_found else 'are NOT'} in output",
            f"Missing: {', '.join(missing_cities)}" if missing_cities else None
        )

        # Test 6: Verify state names appear in output
        expected_states = ['California', 'Arizona', 'Texas', 'New York']

        all_states_found = True
        missing_states = []
        for state in expected_states:
            if state not in stdout:
                all_states_found = False
                missing_states.append(state)

        self.add_test_result(
            "State Names Displayed",
            all_states_found,
            f"All state names "
            f"{'are' if all_states_found else 'are NOT'} in output",
            f"Missing: {', '.join(missing_states)}" if missing_states else None
        )

        # Test 7: Verify results are sorted by cities.id (ascending)
        lines = stdout.strip().split('\n')
        # Skip header line if present
        data_lines = [
            line for line in lines
            if line and not line.startswith('id')
        ]

        if data_lines:
            try:
                # Extract IDs (first column)
                ids = []
                for line in data_lines:
                    parts = line.split('\t')
                    if parts and parts[0].strip().isdigit():
                        ids.append(int(parts[0].strip()))

                # Check if sorted in ascending order
                is_sorted = ids == sorted(ids)
                self.add_test_result(
                    "Results Sorted by cities.id (Ascending)",
                    is_sorted,
                    f"Results {'are' if is_sorted else 'are NOT'} "
                    "sorted by cities.id in ascending order",
                    f"IDs: {ids}, Expected: {sorted(ids)}" if not is_sorted else None
                )
            except (ValueError, IndexError) as e:
                self.add_test_result(
                    "Results Sorted by ID",
                    False,
                    "Failed to parse IDs from output",
                    str(e)
                )
        else:
            self.add_test_result(
                "Results Sorted by ID",
                False,
                "No data lines found in output"
            )

        # Test 8: Verify output format (cities.id, cities.name, states.name)
        if data_lines:
            first_line = data_lines[0]
            # Should have 3 columns (city id, city name, state name)
            columns = first_line.split('\t')
            has_three_columns = len(columns) >= 3

            self.add_test_result(
                "Output Format (3 columns)",
                has_three_columns,
                f"Output {'has' if has_three_columns else 'does NOT have'} "
                "expected format (cities.id, cities.name, states.name)",
                f"Line: {first_line}" if not has_three_columns else None
            )

            # Test 9: Verify specific city-state relationships
            if has_three_columns:
                # Check San Francisco-California
                sf_line = [
                    line for line in data_lines
                    if 'San Francisco' in line
                ]
                if sf_line:
                    sf_correct = 'California' in sf_line[0]
                    self.add_test_result(
                        "City-State Relationship (San Francisco)",
                        sf_correct,
                        f"San Francisco {'is' if sf_correct else 'is NOT'} "
                        "correctly associated with California",
                        sf_line[0] if not sf_correct else None
                    )

                # Check Phoenix-Arizona
                phx_line = [
                    line for line in data_lines
                    if 'Phoenix' in line
                ]
                if phx_line:
                    phx_correct = 'Arizona' in phx_line[0]
                    self.add_test_result(
                        "City-State Relationship (Phoenix)",
                        phx_correct,
                        f"Phoenix {'is' if phx_correct else 'is NOT'} "
                        "correctly associated with Arizona",
                        phx_line[0] if not phx_correct else None
                    )

                # Check Houston-Texas
                hou_line = [
                    line for line in data_lines
                    if 'Houston' in line
                ]
                if hou_line:
                    hou_correct = 'Texas' in hou_line[0]
                    self.add_test_result(
                        "City-State Relationship (Houston)",
                        hou_correct,
                        f"Houston {'is' if hou_correct else 'is NOT'} "
                        "correctly associated with Texas",
                        hou_line[0] if not hou_correct else None
                    )

        # Test 10: Verify correct number of cities returned
        expected_count = 8
        actual_count = len(data_lines)

        self.add_test_result(
            "Correct Number of Cities",
            actual_count == expected_count,
            f"Query returned {actual_count} cities "
            f"(expected {expected_count})",
            stdout if actual_count != expected_count else None
        )

        # Test 11: Verify JOIN is used correctly (no cartesian product)
        # If cartesian product: 4 states * 8 cities = 32 rows
        not_cartesian = actual_count < 20  # Should be 8, not 32

        self.add_test_result(
            "JOIN Used Correctly (Not Cartesian Product)",
            not_cartesian,
            f"JOIN {'is' if not_cartesian else 'is NOT'} "
            "implemented correctly",
            f"{actual_count} rows; cartesian = 32" if not not_cartesian else None
        )
