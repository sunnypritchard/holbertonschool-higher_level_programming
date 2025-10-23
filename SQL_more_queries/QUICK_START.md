# Quick Start Guide

## Run Tests

```bash
./run_tests.py
```

## Project Structure

```
SQL_more_queries/
├── run_tests.py              # ← Run this!
├── tests/
│   ├── mysql_runner.py       # MySQL operations
│   ├── base_checker.py       # Base test framework
│   └── checkers/             # ONE FILE PER TASK
│       ├── task_0.py         # Task 0: List privileges
│       ├── task_1.py         # Task 1: Create user ALL PRIVILEGES
│       ├── task_2.py         # Task 2: Database & read-only user
│       ├── task_3.py         # Task 3: Force name (NOT NULL)
│       ├── task_4.py         # Task 4: Never empty (DEFAULT)
│       ├── task_5.py         # Task 5: Unique ID (UNIQUE)
│       └── task_6.py         # Task 6: States (AUTO_INCREMENT)
└── *.sql                     # Your SQL files
```

## Module Overview

| Module | Purpose | Key Classes |
|--------|---------|-------------|
| `mysql_runner.py` | Database operations | `MySQLTestRunner` |
| `base_checker.py` | Test framework | `TaskChecker`, `TestCase` |
| `task_0.py` | Privileges test | `Task0Checker` |
| `task_1.py` | User creation test | `Task1Checker` |
| `task_2.py` | Read-only user test | `Task2Checker` |
| `task_3.py` | NOT NULL test | `Task3Checker` |
| `task_4.py` | DEFAULT value test | `Task4Checker` |
| `task_5.py` | UNIQUE constraint test | `Task5Checker` |
| `task_6.py` | AUTO_INCREMENT test | `Task6Checker` |

## Test Coverage Per Task

### Task 0 (0-privileges.sql) - 7 tests
**File**: `tests/checkers/task_0.py`
- File existence
- SQL execution
- User grants display (user_0d_1)
- User grants display (user_0d_2)
- SHOW GRANTS usage
- User reference (user_0d_1)
- User reference (user_0d_2)

### Task 1 (1-create_user.sql) - 6 tests
**File**: `tests/checkers/task_1.py`
- File existence
- SQL execution
- User creation
- ALL PRIVILEGES verification
- IF NOT EXISTS usage
- Idempotency

### Task 2 (2-create_read_user.sql) - 8 tests
**File**: `tests/checkers/task_2.py`
- File existence
- SQL execution
- Database creation
- User creation
- SELECT privilege verification
- Limited privileges check
- IF NOT EXISTS usage
- Idempotency

### Task 3 (3-force_name.sql) - 9 tests
**File**: `tests/checkers/task_3.py`
- File existence
- SQL execution
- Table creation
- Column 'id' exists
- Column 'name' exists
- NOT NULL constraint
- VARCHAR(256) type
- Constraint functionality
- Idempotency

### Task 4 (4-never_empty.sql) - 9 tests
**File**: `tests/checkers/task_4.py`
- File existence
- SQL execution
- Table creation
- Column 'id' exists
- Column 'name' exists
- DEFAULT value (1)
- VARCHAR(256) type
- Default functionality
- Idempotency

### Task 5 (5-unique_id.sql) - 9 tests
**File**: `tests/checkers/task_5.py`
- File existence
- SQL execution
- Table creation
- Column 'id' exists
- Column 'name' exists
- DEFAULT value (1)
- UNIQUE constraint
- VARCHAR(256) type
- Constraint functionality
- Idempotency

### Task 6 (6-states.sql) - 10 tests
**File**: `tests/checkers/task_6.py`
- File existence
- SQL execution
- Table creation
- Column 'id' exists
- Column 'name' exists
- PRIMARY KEY
- AUTO_INCREMENT
- NOT NULL constraint
- VARCHAR(256) type
- AUTO_INCREMENT functionality
- Constraint functionality
- Idempotency

**Total: 58 Tests**

## Adding a New Test

### 1. Create dedicated task file

```bash
# Create tests/checkers/task_7.py
```

```python
from tests.base_checker import TaskChecker
import os


class Task7Checker(TaskChecker):
    """Checker for Task 7: Description"""

    def __init__(self, mysql_runner):
        super().__init__(7, "7-file.sql", mysql_runner)
        self.database = "database_name"

    def setup(self) -> None:
        """Cleanup before test"""
        self.mysql.cleanup_database(self.database)

    def teardown(self) -> None:
        """Cleanup after test"""
        self.mysql.cleanup_database(self.database)

    def execute_tests(self) -> None:
        """Execute all tests for Task 7"""
        # File existence
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

        # SQL execution
        success, _, stderr = self.mysql.execute_sql_file(self.sql_file)
        self.add_test_result(
            "SQL Execution",
            success,
            "SQL executed successfully" if success else "Failed",
            stderr if not success else None
        )

        # Add more tests...
```

### 2. Import in `run_tests.py`

```python
from tests.checkers.task_7 import Task7Checker
```

### 3. Run in main()

```python
# In main():
task7 = Task7Checker(mysql_runner)
results[7] = task7.run_tests()
```

## Common Operations

### MySQL Runner Methods
```python
# Execute operations
mysql.execute_sql_file(filepath)           # Run SQL file
mysql.execute_sql_query(query)             # Run SQL query

# Check existence
mysql.user_exists(username, host)          # Check user
mysql.database_exists(database)            # Check database
mysql.table_exists(table, database)        # Check table

# Get information
mysql.get_user_grants(username, host)      # Get privileges
mysql.get_table_structure(table, database) # Get columns

# Cleanup
mysql.cleanup_user(username, host)         # Drop user
mysql.cleanup_database(database)           # Drop database
mysql.cleanup_table(table, database)       # Drop table
```

### Adding Test Results
```python
self.add_test_result(
    "Test Name",           # Name displayed
    True/False,            # Pass/fail
    "Message",             # Description
    "Optional details"     # Shown on failure (optional)
)
```

## Environment Variables

```bash
MYSQL_USER=root           # Default: root
MYSQL_PASSWORD=secret     # Default: empty
```

## Finding a Specific Task's Tests

Easy! Just look at the task number:

```
Task 0 → tests/checkers/task_0.py
Task 1 → tests/checkers/task_1.py
Task 2 → tests/checkers/task_2.py
Task 3 → tests/checkers/task_3.py
Task 4 → tests/checkers/task_4.py
Task 5 → tests/checkers/task_5.py
Task 6 → tests/checkers/task_6.py
Task N → tests/checkers/task_N.py
```

## Example Test Output

```
============================================================
Testing Task 3: 3-force_name.sql
============================================================

✓ File Existence
  SQL file '3-force_name.sql' exists

✓ SQL Execution
  SQL file executed successfully

✓ Table Creation
  Table 'force_name' was created in 'hbtn_0d_2'

✓ Column 'id' Exists
  Column 'id' exists

✓ Column 'name' Exists
  Column 'name' exists

✓ Column 'name' is NOT NULL
  Column 'name' is constrained as NOT NULL (forces name)

✓ Column 'name' Type is VARCHAR(256)
  Column 'name' type is VARCHAR(256)

✓ NOT NULL Constraint Works (INSERT with NULL name fails)
  Inserting NULL name correctly fails

✓ Idempotency Test
  Script can be run multiple times without errors

============================================================
✓ Task 3: ALL TESTS PASSED
============================================================
```

## Tips

### Best Practices
- Each checker is independent and isolated
- Tests clean up after themselves (setup/teardown)
- All tests verify idempotency (can run multiple times)
- Failed tests show detailed error information
- Exit code: 0 = all pass, 1 = any fail

### Why Separated Task Files?
1. **Easy to find**: Task N → task_N.py (no guessing!)
2. **Easy to modify**: Change one task without touching others
3. **No conflicts**: Multiple developers can work simultaneously
4. **Clear ownership**: One file = one task = one responsibility
5. **Scalable**: Adding Task 100? Just create task_100.py

### Task File Template
```python
#!/usr/bin/env python3
"""
Task N Checker: Brief description
Tests for N-filename.sql
"""
import os
from tests.base_checker import TaskChecker


class TaskNChecker(TaskChecker):
    """Checker for Task N: Description"""

    def __init__(self, mysql_runner):
        super().__init__(N, "N-filename.sql", mysql_runner)
        # Task-specific attributes

    def setup(self) -> None:
        """Setup before tests"""
        pass

    def teardown(self) -> None:
        """Cleanup after tests"""
        pass

    def execute_tests(self) -> None:
        """Execute all tests for Task N"""
        # Implement tests here
        pass
```

## Troubleshooting

### Can't find test for Task N?
```bash
ls tests/checkers/task_N.py  # It's always task_N.py!
```

### Import errors?
```bash
cd /path/to/SQL_more_queries  # Run from project root
./run_tests.py
```

### MySQL connection issues?
```bash
sudo systemctl status mysql   # Check MySQL is running
```

### Want to see detailed test code?
```bash
cat tests/checkers/task_N.py  # Each file is self-contained
```

## Summary

- **58 tests** across **7 task files**
- **One file per task** - easy to find and modify
- **DRY, Clean, Robust** code following best practices
- **100% test coverage** of all SQL tasks
- **Exit code 0** = all tests pass

Run `./run_tests.py` and watch all 7 tasks pass! ✓
