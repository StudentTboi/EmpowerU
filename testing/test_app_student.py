"""
EmpowerU

This file contains the tests for the StudentUser class definition.
"""

# Standard library imports
import sys
sys.path.append("../app")

# Related third party imports
import pytest

# Local application imports
from app_student import StudentUser

def test_authenticate():
    """
    Test cases for the authenticate() static method
	Update: the path_to_root argument value must be set to ".."
    """
    # TODO: at least 5 assert statements for the authenticate() static method
    ta1= StudentUser.authenticate("kristinp","kr1st1np")
    assert ta1 is not None
    ta2= StudentUser.authenticate("kristinp","kristinp")
    assert ta2 is None
    ta3= StudentUser.authenticate("kr1st1np","kr1st1np")
    assert ta3 is None


