#!/usr/bin/env python3
"""
Base Task Checker Module
Provides base class for all task checkers
"""
from typing import List, Optional
from dataclasses import dataclass
from enum import Enum


class TestResult(Enum):
    """Test result status"""
    PASS = "✓"
    FAIL = "✗"
    ERROR = "⚠"


@dataclass
class TestCase:
    """Represents a single test case"""
    name: str
    passed: bool
    message: str
    details: Optional[str] = None


class TaskChecker:
    """Base class for task checkers"""

    def __init__(self, task_number: int, sql_file: str, mysql_runner):
        self.task_number = task_number
        self.sql_file = sql_file
        self.mysql = mysql_runner
        self.test_cases: List[TestCase] = []

    def setup(self) -> None:
        """Setup before running tests - override in subclasses"""
        pass

    def teardown(self) -> None:
        """Cleanup after running tests - override in subclasses"""
        pass

    def run_tests(self) -> bool:
        """Run all tests for this task"""
        print(f"\n{'='*60}")
        print(f"Testing Task {self.task_number}: {self.sql_file}")
        print(f"{'='*60}")

        self.setup()

        try:
            self.execute_tests()
        except Exception as e:
            self.test_cases.append(TestCase(
                name="Execution Error",
                passed=False,
                message=f"Error during test execution: {str(e)}"
            ))
        finally:
            self.teardown()

        return self.print_results()

    def execute_tests(self) -> None:
        """Execute the actual tests - must be implemented in subclasses"""
        raise NotImplementedError("Subclasses must implement execute_tests()")

    def add_test_result(self, name: str, passed: bool, message: str, details: str = None) -> None:
        """Add a test result"""
        self.test_cases.append(TestCase(name, passed, message, details))

    def print_results(self) -> bool:
        """Print test results and return overall pass/fail"""
        all_passed = True

        for test in self.test_cases:
            status = TestResult.PASS if test.passed else TestResult.FAIL
            print(f"\n{status.value} {test.name}")
            print(f"  {test.message}")
            if test.details:
                print(f"  Details: {test.details}")

            if not test.passed:
                all_passed = False

        print(f"\n{'='*60}")
        if all_passed:
            print(f"✓ Task {self.task_number}: ALL TESTS PASSED")
        else:
            print(f"✗ Task {self.task_number}: SOME TESTS FAILED")
        print(f"{'='*60}\n")

        return all_passed
