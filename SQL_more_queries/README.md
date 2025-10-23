# SQL More Queries - Test Framework

## Overview

A comprehensive, modular, and scalable test framework for SQL tasks. The framework is designed following DRY principles with **separated task files** for maximum maintainability, clarity, and single responsibility.

## Project Structure

```
SQL_more_queries/
├── run_tests.py                    # Main test runner (executable)
├── tests/                          # Test framework package
│   ├── __init__.py                 # Package initialization
│   ├── mysql_runner.py             # MySQL database operations
│   ├── base_checker.py             # Base checker class and utilities
│   └── checkers/                   # Task-specific checkers (ONE FILE PER TASK)
│       ├── __init__.py             # Checker exports
│       ├── task_0.py               # Task 0: List privileges
│       ├── task_1.py               # Task 1: Create user with ALL PRIVILEGES
│       ├── task_2.py               # Task 2: Create database & read-only user
│       ├── task_3.py               # Task 3: Force name (NOT NULL)
│       ├── task_4.py               # Task 4: Never empty (DEFAULT)
│       ├── task_5.py               # Task 5: Unique ID (UNIQUE constraint)
│       └── task_6.py               # Task 6: States (AUTO_INCREMENT)
├── 0-privileges.sql                # SQL task files
├── 1-create_user.sql
├── 2-create_read_user.sql
├── 3-force_name.sql
├── 4-never_empty.sql
├── 5-unique_id.sql
└── 6-states.sql
```

## Module Descriptions

### Core Modules

#### `tests/mysql_runner.py`
**Purpose**: Handles all MySQL database operations
- Execute SQL files and queries
- Database/table/user existence checks
- Cleanup operations
- Metadata retrieval (grants, table structure)

**Key Class**: `MySQLTestRunner`

#### `tests/base_checker.py`
**Purpose**: Provides base functionality for all task checkers
- Test execution framework
- Setup/teardown lifecycle management
- Result tracking and reporting
- Standardized output formatting

**Key Classes**: `TaskChecker`, `TestCase`, `TestResult`

### Task Checker Modules (Separated by Task)

Each task has its own dedicated file for clarity and maintainability:

#### `tests/checkers/task_0.py`
**Task 0**: List user privileges
- **Class**: `Task0Checker`
- **Tests**: 7 comprehensive checks
- **Validates**: SHOW GRANTS usage, output format, user references

#### `tests/checkers/task_1.py`
**Task 1**: Create user with all privileges
- **Class**: `Task1Checker`
- **Tests**: 6 comprehensive checks
- **Validates**: User creation, ALL PRIVILEGES, IF NOT EXISTS, idempotency

#### `tests/checkers/task_2.py`
**Task 2**: Create database and user with SELECT privilege
- **Class**: `Task2Checker`
- **Tests**: 8 comprehensive checks
- **Validates**: Database creation, SELECT-only privilege, no dangerous privileges

#### `tests/checkers/task_3.py`
**Task 3**: Create table with NOT NULL constraint
- **Class**: `Task3Checker`
- **Tests**: 9 comprehensive checks
- **Validates**: Table creation, NOT NULL constraint functionality

#### `tests/checkers/task_4.py`
**Task 4**: Create table with DEFAULT value
- **Class**: `Task4Checker`
- **Tests**: 9 comprehensive checks
- **Validates**: DEFAULT value of 1, ensures id is never empty

#### `tests/checkers/task_5.py`
**Task 5**: Create table with UNIQUE constraint
- **Class**: `Task5Checker`
- **Tests**: 9 comprehensive checks
- **Validates**: UNIQUE constraint prevents duplicates

#### `tests/checkers/task_6.py`
**Task 6**: Create table with AUTO_INCREMENT PRIMARY KEY
- **Class**: `Task6Checker`
- **Tests**: 10 comprehensive checks
- **Validates**: AUTO_INCREMENT, PRIMARY KEY, sequential ID generation

## Usage

### Running Tests

Run all tests:
```bash
./run_tests.py
```

Or:
```bash
python3 run_tests.py
```

### Custom MySQL Credentials

Set environment variables:
```bash
export MYSQL_USER=your_username
export MYSQL_PASSWORD=your_password
./run_tests.py
```

Or inline:
```bash
MYSQL_USER=root MYSQL_PASSWORD=secret ./run_tests.py
```

## Test Coverage Summary

**Total: 58 Test Cases Across 7 Tasks**

| Task | SQL File | Checker | Tests | Key Validations |
|------|----------|---------|-------|-----------------|
| 0 | 0-privileges.sql | Task0Checker | 7 | SHOW GRANTS, output format |
| 1 | 1-create_user.sql | Task1Checker | 6 | User creation, ALL PRIVILEGES |
| 2 | 2-create_read_user.sql | Task2Checker | 8 | Database, SELECT-only user |
| 3 | 3-force_name.sql | Task3Checker | 9 | NOT NULL constraint |
| 4 | 4-never_empty.sql | Task4Checker | 9 | DEFAULT value |
| 5 | 5-unique_id.sql | Task5Checker | 9 | UNIQUE constraint |
| 6 | 6-states.sql | Task6Checker | 10 | AUTO_INCREMENT, PRIMARY KEY |

Each task is comprehensively tested for:
- ✓ File existence
- ✓ SQL syntax and execution
- ✓ Expected objects created (users, databases, tables)
- ✓ Proper constraints and data types
- ✓ Constraint functionality (NOT NULL, UNIQUE, DEFAULT, etc.)
- ✓ Best practices (IF NOT EXISTS)
- ✓ Idempotency (can run multiple times without errors)

## Adding New Tests

### Step 1: Create a New Task File

Create a dedicated file for your task:

```python
# tests/checkers/task_7.py
from tests.base_checker import TaskChecker


class Task7Checker(TaskChecker):
    """Checker for Task 7: Your task description"""

    def __init__(self, mysql_runner):
        super().__init__(7, "7-filename.sql", mysql_runner)
        # Initialize task-specific attributes
        self.database = "database_name"
        self.table = "table_name"

    def setup(self) -> None:
        """Setup before tests"""
        # Cleanup or prepare resources
        self.mysql.cleanup_database(self.database)

    def teardown(self) -> None:
        """Cleanup after tests"""
        # Clean up resources
        self.mysql.cleanup_database(self.database)

    def execute_tests(self) -> None:
        """Execute tests for Task 7"""
        # Test 1: File existence
        if not os.path.exists(self.sql_file):
            self.add_test_result(
                "File Existence",
                False,
                f"SQL file '{self.sql_file}' not found"
            )
            return

        # Test 2: Execute SQL
        success, _, stderr = self.mysql.execute_sql_file(self.sql_file)
        self.add_test_result(
            "SQL Execution",
            success,
            "SQL executed successfully" if success else "Failed to execute",
            stderr if not success else None
        )

        # Add more tests...
```

### Step 2: Update Main Runner

Update `run_tests.py`:
```python
from tests.checkers.task_7 import Task7Checker

# In main():
task7 = Task7Checker(mysql_runner)
results[7] = task7.run_tests()
```

## Design Principles

### Single Responsibility
- **One file per task** - each task checker has its own file
- Each module has a single, well-defined responsibility
- Easy to locate and modify specific functionality

### DRY (Don't Repeat Yourself)
- Common MySQL operations in `MySQLTestRunner`
- Base test framework in `TaskChecker`
- Reusable utilities and helper methods
- No code duplication across task files

### Modularity
- Separated task files for independent development
- Clear boundaries between components
- Each task can be modified without affecting others

### Scalability
- Simple to add new task checkers (just create new file)
- Modular structure supports unlimited growth
- Clear separation of concerns

### Maintainability
- **Easy to find**: One file per task - no guessing
- Well-documented code with comprehensive docstrings
- Consistent naming conventions (task_N.py)
- Type hints for clarity
- Clean code structure

## Output Format

### Individual Test Output
```
============================================================
Testing Task 1: 1-create_user.sql
============================================================

✓ File Existence
  SQL file '1-create_user.sql' exists

✓ SQL Execution
  SQL file executed successfully

✓ User Creation
  User 'user_0d_1'@'localhost' was created

✓ ALL PRIVILEGES Granted
  User has ALL PRIVILEGES (or equivalent comprehensive privileges)

✓ Uses IF NOT EXISTS
  Script uses IF NOT EXISTS

✓ Idempotency Test
  Script can be run multiple times without errors

============================================================
✓ Task 1: ALL TESTS PASSED
============================================================
```

### Final Summary
```
============================================================
FINAL SUMMARY
============================================================
Task 0: ✓ PASS
Task 1: ✓ PASS
Task 2: ✓ PASS
Task 3: ✓ PASS
Task 4: ✓ PASS
Task 5: ✓ PASS
Task 6: ✓ PASS

Total: 7/7 tasks passed
============================================================
```

## Requirements

- Python 3.x
- MySQL Server
- MySQL user with appropriate privileges (CREATE, DROP, GRANT)

## Troubleshooting

### Import Errors
Ensure you run from the SQL_more_queries directory:
```bash
cd /path/to/SQL_more_queries
./run_tests.py
```

### MySQL Connection
- Verify MySQL server is running: `sudo systemctl status mysql`
- Check credentials are correct
- Ensure user has CREATE, DROP, GRANT privileges

### Test Failures
- Review error details in output (shown with ✗ symbol)
- Check SQL file syntax
- Verify file paths are correct
- Look at "Details" section for specific error messages

### Finding Specific Task Test
With separated files, finding a specific task's tests is simple:
```
tests/checkers/task_N.py  # where N is the task number
```

## Exit Codes

- **0**: All tests passed ✓
- **1**: One or more tests failed ✗

## Benefits of Separated Task Files

### 1. **Clarity**
   - Instantly find the test for any task
   - No need to search through grouped files
   - Clear one-to-one mapping: task N → task_N.py

### 2. **Independence**
   - Modify one task without touching others
   - No merge conflicts when multiple developers work on different tasks
   - Each task is completely self-contained

### 3. **Maintainability**
   - Smaller, focused files are easier to understand
   - Less cognitive load when working on a specific task
   - Clear scope boundaries

### 4. **Testability**
   - Can test individual task checkers in isolation
   - Easy to run specific task tests during development
   - Clear test ownership

### 5. **Scalability**
   - Adding task 100? Just create task_100.py
   - No need to reorganize existing files
   - Linear growth, no complexity increase

## License

Educational use only - Holberton School SQL Project.
