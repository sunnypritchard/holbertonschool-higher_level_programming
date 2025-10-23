#!/usr/bin/env python3
"""
Main Test Runner
Comprehensive SQL Task Checker for SQL_more_queries
"""
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


from tests.mysql_runner import MySQLTestRunner
from tests.checkers.task_0 import Task0Checker
from tests.checkers.task_1 import Task1Checker
from tests.checkers.task_2 import Task2Checker
from tests.checkers.task_3 import Task3Checker
from tests.checkers.task_4 import Task4Checker
from tests.checkers.task_5 import Task5Checker
from tests.checkers.task_6 import Task6Checker
from tests.checkers.task_7 import Task7Checker
from tests.checkers.task_8 import Task8Checker
from tests.checkers.task_9 import Task9Checker


def main():
    """Main test runner"""
    # Parse command line arguments
    task_to_run = None
    if len(sys.argv) > 1:
        try:
            task_to_run = int(sys.argv[1])
            if task_to_run < 0 or task_to_run > 9:
                print(f"Error: Task number must be between 0 and 9")
                print("Usage: python run_tests.py [task_number]")
                sys.exit(1)
        except ValueError:
            print(f"Error: Invalid task number '{sys.argv[1]}'")
            print("Usage: python run_tests.py [task_number]")
            sys.exit(1)

    print("\n" + "="*60)
    if task_to_run is not None:
        print(f"SQL More Queries - Testing Task {task_to_run}")
    else:
        print("SQL More Queries - Comprehensive Task Checker")
    print("="*60)

    # Get MySQL credentials from environment or use defaults
    mysql_user = os.getenv("MYSQL_USER", "root")
    mysql_password = os.getenv("MYSQL_PASSWORD", "")

    # Initialize MySQL runner
    mysql_runner = MySQLTestRunner(mysql_user, mysql_password)

    # Map of task numbers to checker classes
    task_checkers = {
        0: Task0Checker,
        1: Task1Checker,
        2: Task2Checker,
        3: Task3Checker,
        4: Task4Checker,
        5: Task5Checker,
        6: Task6Checker,
        7: Task7Checker,
        8: Task8Checker,
        9: Task9Checker,
    }

    # Test tasks
    results = {}

    # Run specific task or all tasks
    if task_to_run is not None:
        # Run single task
        checker_class = task_checkers[task_to_run]
        checker = checker_class(mysql_runner)
        results[task_to_run] = checker.run_tests()
    else:
        # Run all tasks
        for task_num, checker_class in task_checkers.items():
            checker = checker_class(mysql_runner)
            results[task_num] = checker.run_tests()

    # Print final summary
    print("\n" + "="*60)
    print("FINAL SUMMARY")
    print("="*60)

    total_tasks = len(results)
    passed_tasks = sum(1 for passed in results.values() if passed)

    for task_num, passed in results.items():
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"Task {task_num}: {status}")

    print(f"\nTotal: {passed_tasks}/{total_tasks} tasks passed")
    print("="*60 + "\n")

    # Exit with appropriate code
    sys.exit(0 if passed_tasks == total_tasks else 1)


if __name__ == "__main__":
    main()
