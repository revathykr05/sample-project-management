#!/usr/bin/env python3
"""
Simple Grade Calculator

Features:
- Interactive CLI to enter marks for N subjects (default each subject is out of 100).
- Validates input.
- Calculates total, percentage, letter grade and GPA (4.0 scale).
- Also exposes a `calculate_grade` function you can import/use in other scripts.
"""

from typing import List, Optional, Tuple


def percentage_from_marks(marks: List[float], max_marks: Optional[List[float]] = None) -> float:
    if max_marks is None:
        max_marks =

