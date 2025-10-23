#!/usr/bin/env python3
"""
Task 8 Checker: List cities of California using subquery
Tests for 8-cities_of_california_subquery.sql
"""
import os
from tests.base_checker import TaskChecker


class Task8Checker(TaskChecker):
    """Checker for Task 8: List all cities of California using subquery"""

    def __init__(self, mysql_runner):
        super().__init__(8, "8-cities_of_california_subquery.sql", mysql_runner)
        self.database = "hbtn_0d_usa"
        self.states_table = "states"
        self.cities_table = "cities"

    def setup(self) -> None:
        """Setup: Create database and tables with test data"""
        # Create database
        self.mysql.execute_sql_query(f"CREATE DATABASE IF NOT EXISTS {self.database};")

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

        # Insert test cities
        # California cities (state_id = 1)
        self.mysql.execute_sql_query(
            f"INSERT INTO {self.database}.{self.cities_table} (state_id, name) VALUES "
            "(1, 'San Francisco'), "
            "(1, 'San Jose'), "
            "(2, 'Phoenix'), "
            "(1, 'Los Angeles'), "
            "(3, 'Houston'), "
            "(1, 'San Diego'), "
            "(4, 'New York City'), "
            "(2, 'Tucson');"
        )

    def teardown(self) -> None:
        """Cleanup: Remove tables and database"""
        self.mysql.cleanup_table(self.cities_table, self.database)
        self.mysql.cleanup_table(self.states_table, self.database)
        self.mysql.cleanup_database(self.database)

    def execute_tests(self) -> None:
        """Execute all tests for Task 8"""
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

        # Test 2: Verify script does NOT use JOIN keyword
        with open(self.sql_file, 'r') as f:
            content = f.read()

        # Remove comments before checking for JOIN
        lines = content.split('\n')
        sql_lines = [line.split('--')[0] for line in lines]  # Remove -- comments
        sql_code = '\n'.join(sql_lines).upper()

        has_join = 'JOIN' in sql_code
        self.add_test_result(
            "No JOIN Keyword Used",
            not has_join,
            f"Script {'does NOT use' if not has_join else 'INCORRECTLY uses'} "
            "JOIN keyword",
            "Script must use subquery instead of JOIN" if has_join else None
        )

        # Test 3: Verify script uses subquery (SELECT within SELECT)
        # Count occurrences of SELECT
        select_count = content.count('SELECT')
        uses_subquery = select_count >= 2
        self.add_test_result(
            "Uses Subquery",
            uses_subquery,
            f"Script {'uses' if uses_subquery else 'does NOT use'} subquery (found {select_count} SELECT statement(s))",
            "Script must use a subquery to find California's id" if not uses_subquery else None
        )

        # Test 4: Execute SQL file with database parameter
        success, stdout, stderr = self.mysql.execute_sql_file(self.sql_file, self.database)

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

        # Test 5: Verify output contains expected California cities
        expected_ca_cities = ['San Francisco', 'San Jose', 'Los Angeles', 'San Diego']

        for city in expected_ca_cities:
            city_in_output = city in stdout
            self.add_test_result(
                f"California City Listed ({city})",
                city_in_output,
                f"City '{city}' {'is' if city_in_output else 'is NOT'} in output",
                stdout if not city_in_output else None
            )

        # Test 6: Verify output does NOT contain non-California cities
        non_ca_cities = ['Phoenix', 'Houston', 'New York City', 'Tucson']

        all_excluded = True
        excluded_details = []
        for city in non_ca_cities:
            if city in stdout:
                all_excluded = False
                excluded_details.append(city)

        self.add_test_result(
            "Non-California Cities Excluded",
            all_excluded,
            f"Non-California cities {'are correctly' if all_excluded else 'are NOT'} excluded",
            f"Found non-CA cities in output: {', '.join(excluded_details)}" if not all_excluded else None
        )

        # Test 7: Verify results are sorted by cities.id (ascending order)
        # Extract city IDs from output
        lines = stdout.strip().split('\n')
        # Skip header line if present
        data_lines = [line for line in lines if line and not line.startswith('id')]

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
                    "Results Sorted by ID (Ascending)",
                    is_sorted,
                    f"Results {'are' if is_sorted else 'are NOT'} sorted by cities.id in ascending order",
                    f"IDs in output: {ids}, Expected: {sorted(ids)}" if not is_sorted else None
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

        # Test 8: Verify correct number of California cities returned
        # We inserted 4 California cities
        expected_count = 4
        actual_count = len(data_lines)

        self.add_test_result(
            "Correct Number of Cities",
            actual_count == expected_count,
            f"Query returned {actual_count} cities (expected {expected_count})",
            stdout if actual_count != expected_count else None
        )

        # Test 9: Verify output format (should have id and name columns)
        if data_lines:
            first_line = data_lines[0]
            # Should have at least 2 columns (id and name)
            columns = first_line.split('\t')
            has_two_columns = len(columns) >= 2
            self.add_test_result(
                "Output Format (id and name columns)",
                has_two_columns,
                f"Output {'has' if has_two_columns else 'does NOT have'} expected format (id, name)",
                f"First line: {first_line}" if not has_two_columns else None
            )

        # Test 10: Test with different California id (ensure it's truly using subquery)
        # Clean up and recreate with California having different id
        self.mysql.cleanup_table(self.cities_table, self.database)
        self.mysql.cleanup_table(self.states_table, self.database)

        # Recreate states table
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

        # Insert states with different order (California is now id=3)
        self.mysql.execute_sql_query(
            f"INSERT INTO {self.database}.{self.states_table} (name) VALUES "
            "('Texas'), ('Arizona'), ('California'), ('New York');"
        )

        # Insert cities (California cities now have state_id=3)
        self.mysql.execute_sql_query(
            f"INSERT INTO {self.database}.{self.cities_table} (state_id, name) VALUES "
            "(1, 'Houston'), "
            "(2, 'Phoenix'), "
            "(3, 'Sacramento'), "
            "(3, 'Oakland'), "
            "(4, 'Buffalo');"
        )

        # Execute query again
        success2, stdout2, stderr2 = self.mysql.execute_sql_file(self.sql_file, self.database)

        if success2:
            # Should still find California cities even though id changed
            ca_found = 'Sacramento' in stdout2 and 'Oakland' in stdout2
            non_ca_excluded = 'Houston' not in stdout2 and 'Phoenix' not in stdout2 and 'Buffalo' not in stdout2

            self.add_test_result(
                "Subquery Works with Different State IDs",
                ca_found and non_ca_excluded,
                f"Query {'correctly' if (ca_found and non_ca_excluded) else 'does NOT'} find California cities when state_id changes",
                stdout2 if not (ca_found and non_ca_excluded) else None
            )
        else:
            self.add_test_result(
                "Subquery Test with Different IDs",
                False,
                "Failed to execute query with different state IDs",
                stderr2
            )
