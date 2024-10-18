"""
EmpowerU

This file contains the tests for the AdministratorUser class definition.
"""

# Standard library imports
import sys
sys.path.append("../app")

# Related third party imports
import pytest

# Local application imports
from app.app_administrator import AdministratorUser

def test_authenticate():
    """
    Test cases for the authenticate() static method
	Update: the path_to_root argument value must be set to ".."
    """
    # TODO: at least 5 assert statements for the authenticate() static method
    ta1= AdministratorUser.authenticate("lilo","l1l0")
    assert ta1 is not None
    ta2= AdministratorUser.authenticate("lilo","lilo")
    assert ta2 is None
    ta3= AdministratorUser.authenticate("invce","invc3")
    assert ta3 is not None
    ta4= AdministratorUser.authenticate("invce","l1l0")
    assert ta4 is None
    ta5= AdministratorUser.authenticate("lilo","invc3")
    assert ta5 is None


