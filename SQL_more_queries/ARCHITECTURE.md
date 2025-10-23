# Test Framework Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                      run_tests.py                           │
│                   (Main Entry Point)                        │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │ imports & coordinates
                      ▼
┌─────────────────────────────────────────────────────────────┐
│                   Test Framework Layers                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Layer 1: Core Infrastructure                              │
│  ┌──────────────────┐    ┌──────────────────┐             │
│  │ MySQLTestRunner  │    │  TaskChecker     │             │
│  │ (mysql_runner)   │    │  (base_checker)  │             │
│  │                  │    │                  │             │
│  │ • DB operations  │    │ • Test lifecycle │             │
│  │ • Queries        │    │ • Result tracking│             │
│  │ • Cleanup        │    │ • Reporting      │             │
│  └──────────────────┘    └──────────────────┘             │
│          ▲                        ▲                        │
│          │                        │                        │
│          └────────┬───────────────┘                        │
│                   │ inherited by                           │
│  Layer 2: Individual Task Checkers (ONE FILE PER TASK)    │
│  ┌────────────────────────────────────────────────┐       │
│  │         tests/checkers/                        │       │
│  │                                                │       │
│  │  task_0.py  task_2.py  task_4.py  task_6.py  │       │
│  │  task_1.py  task_3.py  task_5.py              │       │
│  │  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ │       │
│  │  │ Task0  │ │ Task2  │ │ Task4  │ │ Task6  │ │       │
│  │  │Checker │ │Checker │ │Checker │ │Checker │ │       │
│  │  └────────┘ └────────┘ └────────┘ └────────┘ │       │
│  │  ┌────────┐ ┌────────┐ ┌────────┐            │       │
│  │  │ Task1  │ │ Task3  │ │ Task5  │            │       │
│  │  │Checker │ │Checker │ │Checker │            │       │
│  │  └────────┘ └────────┘ └────────┘            │       │
│  └────────────────────────────────────────────────┘       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## File Structure

```
tests/
├── __init__.py
├── mysql_runner.py              # Layer 1: Database operations
├── base_checker.py              # Layer 1: Test framework
└── checkers/                    # Layer 2: Task implementations
    ├── __init__.py
    ├── task_0.py                # ← One file per task
    ├── task_1.py                # ← Separated for clarity
    ├── task_2.py                # ← Easy to find
    ├── task_3.py                # ← Single responsibility
    ├── task_4.py                # ← Independent development
    ├── task_5.py                # ← No merge conflicts
    └── task_6.py                # ← Scalable structure
```

## Component Responsibilities

### 1. MySQLTestRunner (Infrastructure)
**File**: `tests/mysql_runner.py`
**Purpose**: Centralized MySQL database operations

```
MySQLTestRunner
├── Connection Management
│   ├── _build_base_command()
│   └── Credentials handling
│
├── Execution Methods
│   ├── execute_sql_file()
│   └── execute_sql_query()
│
├── Verification Methods
│   ├── user_exists()
│   ├── database_exists()
│   ├── table_exists()
│   ├── get_user_grants()
│   └── get_table_structure()
│
└── Cleanup Methods
    ├── cleanup_user()
    ├── cleanup_database()
    └── cleanup_table()
```

### 2. TaskChecker (Base Framework)
**File**: `tests/base_checker.py`
**Purpose**: Provides test execution framework

```
TaskChecker (Abstract Base)
├── Lifecycle Methods
│   ├── setup()           # Pre-test preparation
│   ├── execute_tests()   # Main test logic (must override)
│   ├── teardown()        # Post-test cleanup
│   └── run_tests()       # Orchestrates flow
│
├── Test Management
│   ├── add_test_result() # Record test outcome
│   └── test_cases[]      # Result storage
│
└── Reporting
    └── print_results()   # Formatted output
```

### 3. Individual Task Checkers (Separated Files)
**Files**: `tests/checkers/task_0.py` through `task_6.py`
**Purpose**: Task-specific test logic (ONE FILE PER TASK)

```
Individual Task Checker (e.g., Task3Checker in task_3.py)
├── __init__()
│   └── Configure task number, SQL file, mysql_runner
│
├── setup()
│   └── Prepare test environment (cleanup existing)
│
├── execute_tests()         ← Core test implementation
│   ├── File existence check
│   ├── SQL execution test
│   ├── Object verification
│   ├── Constraint tests
│   └── Idempotency test
│
└── teardown()
    └── Clean up resources
```

#### Task Checker Breakdown

| File | Class | Task | SQL File | Tests |
|------|-------|------|----------|-------|
| `task_0.py` | Task0Checker | List privileges | 0-privileges.sql | 7 |
| `task_1.py` | Task1Checker | Create user ALL PRIVILEGES | 1-create_user.sql | 6 |
| `task_2.py` | Task2Checker | Database & read-only user | 2-create_read_user.sql | 8 |
| `task_3.py` | Task3Checker | Force name (NOT NULL) | 3-force_name.sql | 9 |
| `task_4.py` | Task4Checker | Never empty (DEFAULT) | 4-never_empty.sql | 9 |
| `task_5.py` | Task5Checker | Unique ID (UNIQUE) | 5-unique_id.sql | 9 |
| `task_6.py` | Task6Checker | States (AUTO_INCREMENT) | 6-states.sql | 10 |

## Data Flow

```
┌─────────────┐
│  run_tests  │
└──────┬──────┘
       │
       │ 1. Initialize MySQLTestRunner
       ▼
┌──────────────────┐
│ MySQLTestRunner  │
└──────┬───────────┘
       │
       │ 2. Pass to each TaskChecker
       ├──► Task0Checker (task_0.py)
       ├──► Task1Checker (task_1.py)
       ├──► Task2Checker (task_2.py)
       ├──► Task3Checker (task_3.py)
       ├──► Task4Checker (task_4.py)
       ├──► Task5Checker (task_5.py)
       └──► Task6Checker (task_6.py)
              │
              │ 3. Run test lifecycle
              ├─────► setup()
              ├─────► execute_tests()
              │         ├─► add_test_result()
              │         ├─► add_test_result()
              │         └─► add_test_result()
              ├─────► teardown()
              └─────► print_results()
                    │
                    ▼
              ┌─────────────┐
              │ Return bool │
              │ (pass/fail) │
              └─────────────┘
```

## Module Dependencies

```
run_tests.py
    │
    ├─► tests/mysql_runner.py
    │       (no dependencies)
    │
    ├─► tests/base_checker.py
    │       (no dependencies)
    │
    └─► tests/checkers/
            ├─► task_0.py  ──► base_checker
            ├─► task_1.py  ──► base_checker
            ├─► task_2.py  ──► base_checker
            ├─► task_3.py  ──► base_checker
            ├─► task_4.py  ──► base_checker
            ├─► task_5.py  ──► base_checker
            └─► task_6.py  ──► base_checker
```

**Note**: Each task file is completely independent from the others.
No cross-task dependencies = No coupling = Easy maintenance!

## Test Execution Flow

```
1. START
   │
2. Load Configuration
   ├─ MySQL credentials (env vars)
   └─ Initialize MySQLTestRunner
   │
3. For Each Task (0-6):
   │
   ├─ Import task_N.py
   │  │
   ├─ Create TaskNChecker instance
   │  │
   │  ├─ 3a. SETUP
   │  │    └─ Clean existing resources
   │  │
   │  ├─ 3b. EXECUTE TESTS
   │  │    ├─ Check file exists
   │  │    ├─ Execute SQL
   │  │    ├─ Verify objects created
   │  │    ├─ Test constraints
   │  │    └─ Test idempotency
   │  │
   │  ├─ 3c. TEARDOWN
   │  │    └─ Clean created resources
   │  │
   │  └─ 3d. REPORT
   │       ├─ Print individual results
   │       └─ Return pass/fail
   │
4. Aggregate Results
   ├─ Count passed/failed
   └─ Print summary
   │
5. EXIT
   └─ Code: 0 (all pass) or 1 (any fail)
```

## Design Patterns

### 1. Template Method Pattern
`TaskChecker.run_tests()` defines the algorithm structure:
- setup() → execute_tests() → teardown() → print_results()
- Subclasses override specific steps

### 2. Strategy Pattern
Each TaskChecker implements its own test strategy in `execute_tests()`

### 3. Facade Pattern
`MySQLTestRunner` provides simplified interface to MySQL operations

### 4. Single Responsibility Principle
- MySQLTestRunner: Database operations only
- TaskChecker: Test framework only
- **task_N.py: Task N testing only** ← Strictly enforced!

## Extension Points

### Adding New Task

**Step 1**: Create `tests/checkers/task_7.py`
```python
#!/usr/bin/env python3
"""
Task 7 Checker: Description
Tests for 7-filename.sql
"""
from tests.base_checker import TaskChecker


class Task7Checker(TaskChecker):
    def __init__(self, mysql_runner):
        super().__init__(7, "7-filename.sql", mysql_runner)

    def execute_tests(self) -> None:
        # Implement tests
        pass
```

**Step 2**: Import in `run_tests.py`
```python
from tests.checkers.task_7 import Task7Checker
```

**Step 3**: Run in main()
```python
task7 = Task7Checker(mysql_runner)
results[7] = task7.run_tests()
```

### Adding New Functionality
1. Add helper method to MySQLTestRunner (if DB-related)
2. Add helper method to TaskChecker (if test-related)
3. Use in task-specific checker

## Benefits of Separated Task Files

### 1. **Clarity & Discoverability**
```
Need to modify Task 3? → Open tests/checkers/task_3.py
No searching, no guessing, instant access!
```

### 2. **Independence & Isolation**
- Modify task_3.py without touching task_1.py or task_5.py
- Each file is completely self-contained
- No ripple effects from changes

### 3. **Parallel Development**
- Developer A works on task_2.py
- Developer B works on task_5.py
- Developer C works on task_7.py
- Zero merge conflicts!

### 4. **Cognitive Load Reduction**
- Small, focused files (100-300 lines each)
- Easy to understand entire file at once
- Clear scope: "This file tests task N and ONLY task N"

### 5. **Scalability**
```
Task 10?  → Create task_10.py
Task 50?  → Create task_50.py
Task 100? → Create task_100.py

No reorganization needed!
Linear growth, no complexity increase.
```

### 6. **Testing & Debugging**
- Can test individual task checkers in isolation
- Easy to run specific task during development
- Clear test ownership and accountability

### 7. **Code Review**
- Reviewers can focus on specific task file
- Smaller diffs = easier reviews
- Clear what changed in which task

## Architecture Comparison

### Before (Grouped Files)
```
checkers/
├── tasks_0_1.py    # 2 tasks, 215 lines
├── tasks_2_3.py    # 2 tasks, 270 lines
└── tasks_4_6.py    # 3 tasks, 502 lines
```
**Issues**:
- Need to search within file for specific task
- Modifying one task touches file used by others
- Larger files = more cognitive load
- Groups are arbitrary

### After (Separated Files)
```
checkers/
├── task_0.py       # 1 task, 117 lines ✓
├── task_1.py       # 1 task, 127 lines ✓
├── task_2.py       # 1 task, 160 lines ✓
├── task_3.py       # 1 task, 162 lines ✓
├── task_4.py       # 1 task, 175 lines ✓
├── task_5.py       # 1 task, 181 lines ✓
└── task_6.py       # 1 task, 242 lines ✓
```
**Benefits**:
- Direct file → task mapping
- Independent modifications
- Smaller, focused files
- Natural organization

## Design Benefits Summary

### Modularity
- ✓ Each component has clear boundaries
- ✓ Easy to locate and modify code
- ✓ Components can evolve independently
- **✓ One file per task = ultimate modularity**

### Reusability
- ✓ MySQLTestRunner used by all checkers
- ✓ TaskChecker provides common framework
- ✓ No code duplication across tasks

### Testability
- ✓ Each component can be tested in isolation
- ✓ Mock MySQLTestRunner for unit testing
- ✓ Clear interfaces
- **✓ Each task file testable independently**

### Scalability
- ✓ Simple to add new tasks
- ✓ Can add new test types easily
- ✓ Supports parallel execution (future)
- **✓ Linear growth: Task N → task_N.py**

### Maintainability
- ✓ Changes localized to specific modules
- ✓ Easy to understand and navigate
- ✓ Well-documented
- **✓ Separated files = easiest maintenance**

## Real-World Example

### Finding and Modifying Task 3

**Old Way** (Grouped):
1. "Which file has task 3?"
2. Open tasks_2_3.py
3. Search for Task3Checker
4. Scroll to find it
5. Modify it
6. Hope you didn't break Task2

**New Way** (Separated):
1. Open tests/checkers/task_3.py
2. Modify it
3. Done! No other tasks affected.

### Code Review

**Old Way**:
```
PR: "Update tasks 2, 3, and 5"
Files changed: tasks_2_3.py, tasks_4_6.py
Lines changed: +50, -30
Reviewer: *scrolls through 270-line file to find changes*
```

**New Way**:
```
PR: "Update tasks 2, 3, and 5"
Files changed: task_2.py, task_3.py, task_5.py
Lines changed: +25, -15 each
Reviewer: *reviews three focused files, immediately sees changes*
```

## Conclusion

The separated task file architecture provides:

1. **Maximum Clarity**: Task N = task_N.py
2. **Maximum Independence**: Each file standalone
3. **Maximum Simplicity**: Small, focused files
4. **Maximum Scalability**: Unlimited tasks, no reorganization
5. **Maximum Maintainability**: Easy to find, easy to modify

**Result**: A test framework that's **DRY, Clean, and Robust** with the added benefit of being **incredibly easy to navigate and maintain**.
