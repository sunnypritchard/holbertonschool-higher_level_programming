#!/usr/bin/env python3
"""
MySQL Test Runner Module
Handles all MySQL database operations for testing
"""
import subprocess
import os
from typing import Dict, List, Tuple, Optional, Any


class MySQLTestRunner:
    """Base class for running MySQL tests"""

    def __init__(self, mysql_user: str = "root", mysql_password: str = ""):
        """Initialize MySQL test runner with credentials"""
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.base_cmd = self._build_base_command()

    def _build_base_command(self) -> List[str]:
        """Build the base MySQL command"""
        cmd = ["mysql"]
        if self.mysql_user:
            cmd.extend(["-u", self.mysql_user])
        if self.mysql_password:
            cmd.extend([f"-p{self.mysql_password}"])
        return cmd

    def execute_sql_file(self, filepath: str, database: Optional[str] = None) -> Tuple[bool, str, str]:
        """
        Execute a SQL file

        Args:
            filepath: Path to the SQL file
            database: Optional database name to use

        Returns:
            Tuple of (success, stdout, stderr)
        """
        if not os.path.exists(filepath):
            return False, "", f"File not found: {filepath}"

        try:
            # Build command with optional database
            cmd = self.base_cmd.copy()
            if database:
                cmd.append(database)

            with open(filepath, 'r') as f:
                result = subprocess.run(
                    cmd,
                    stdin=f,
                    capture_output=True,
                    text=True,
                    timeout=10
                )
            return result.returncode == 0, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", "Command timed out"
        except Exception as e:
            return False, "", str(e)

    def execute_sql_query(self, query: str, database: Optional[str] = None) -> Tuple[bool, str, str]:
        """
        Execute a SQL query directly

        Args:
            query: SQL query to execute
            database: Optional database name

        Returns:
            Tuple of (success, stdout, stderr)
        """
        cmd = self.base_cmd.copy()
        if database:
            cmd.append(database)
        cmd.extend(["-e", query])

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0, result.stdout, result.stderr
        except subprocess.TimeoutExpired:
            return False, "", "Command timed out"
        except Exception as e:
            return False, "", str(e)

    def cleanup_user(self, username: str, host: str = "localhost") -> None:
        """Drop a user if it exists"""
        query = f"DROP USER IF EXISTS '{username}'@'{host}';"
        self.execute_sql_query(query)

    def cleanup_database(self, database: str) -> None:
        """Drop a database if it exists"""
        query = f"DROP DATABASE IF EXISTS {database};"
        self.execute_sql_query(query)

    def cleanup_table(self, table: str, database: Optional[str] = None) -> None:
        """Drop a table if it exists"""
        if database:
            query = f"DROP TABLE IF EXISTS {database}.{table};"
        else:
            query = f"DROP TABLE IF EXISTS {table};"
        self.execute_sql_query(query)

    def user_exists(self, username: str, host: str = "localhost") -> bool:
        """Check if a user exists"""
        query = f"SELECT User FROM mysql.user WHERE User = '{username}' AND Host = '{host}';"
        success, stdout, _ = self.execute_sql_query(query)
        return success and username in stdout

    def database_exists(self, database: str) -> bool:
        """Check if a database exists"""
        query = f"SHOW DATABASES LIKE '{database}';"
        success, stdout, _ = self.execute_sql_query(query)
        return success and database in stdout

    def table_exists(self, table: str, database: Optional[str] = None) -> bool:
        """Check if a table exists"""
        if database:
            query = f"SHOW TABLES FROM {database} LIKE '{table}';"
        else:
            query = f"SHOW TABLES LIKE '{table}';"
        success, stdout, _ = self.execute_sql_query(query)
        return success and table in stdout

    def get_user_grants(self, username: str, host: str = "localhost") -> Tuple[bool, List[str]]:
        """Get grants for a user"""
        query = f"SHOW GRANTS FOR '{username}'@'{host}';"
        success, stdout, _ = self.execute_sql_query(query)
        if success:
            grants = [line.strip() for line in stdout.split('\n') if line.strip() and not line.startswith('Grants')]
            return True, grants
        return False, []

    def get_table_structure(self, table: str, database: Optional[str] = None) -> Tuple[bool, Dict[str, Any]]:
        """Get table structure information"""
        if database:
            query = f"DESCRIBE {database}.{table};"
        else:
            query = f"DESCRIBE {table};"

        success, stdout, _ = self.execute_sql_query(query)
        if not success:
            return False, {}

        structure = {}
        lines = stdout.strip().split('\n')[1:]  # Skip header
        for line in lines:
            if line.strip():
                parts = line.split('\t')
                if len(parts) >= 4:
                    field_name = parts[0]
                    structure[field_name] = {
                        'type': parts[1],
                        'null': parts[2],
                        'key': parts[3],
                        'default': parts[4] if len(parts) > 4 else None,
                        'extra': parts[5] if len(parts) > 5 else None
                    }
        return True, structure
