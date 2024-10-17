"""
EmpowerU

This file contains the tests for the Quiz class definition.
"""

# Standard library imports
import sys
sys.path.append("../app")

# Related third party imports
import pytest

# Local application imports
from app_quiz import Quiz

def test_loadQuizFromFile(filename: str):
  lq1= Quiz.loadQuizFromFile("filename")
  assert lq1 is None

def test_gradeQuiz(self, student_answer: list, studentId: int):
  pass

def givefeedback(self, studentId: int, feedback: str) -> None:
  pass


