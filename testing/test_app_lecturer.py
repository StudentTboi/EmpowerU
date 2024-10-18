"""
EmpowerU

This file contains the tests for the LecturerUser class definition.
"""

# Standard library imports
import sys
sys.path.append("../app")

# Related third party imports
import pytest

# Local application imports
from app.app_lecturer import LecturerUser

def test_authenticate():
    """
    Test cases for the authenticate() static method
	Update: the path_to_root argument value must be set to ".."
    """
    # TODO: at least 5 assert statements for the authenticate() static method
    ta1= LecturerUser.authenticate("tonyc","t0nyc")
    assert ta1 is not None
    ta2= LecturerUser.authenticate("tonyc","tonyc")
    assert ta2 is None
    ta3= LecturerUser.authenticate("t0nyc","t0nyc")
    assert ta3 is None
    



