"""
EmpowerU

This file contains the tests for the StudentUser class definition.
"""

import sys
import os
import pytest
from unittest import mock

# Adding the project root directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Correct import for app_administrator
from app.app_student import StudentUser

@pytest.fixture
def mock_read_file():
    return [
        "s0001;Kristin;Purnell;01/02/2001;0412344320;kris@kris.com;kristinp;kr1st1np;['AI', 'InfoSec', 'PyLearn'];[1, 1, 0, 0, 0, 0]",
        
    ]

@mock.patch("app.app_administrator.util.read_file")
def test_authenticate(mock_read_file_function, mock_read_file):
    mock_read_file_function.return_value = mock_read_file

    ta1 = StudentUser.authenticate("kristinp", "kr1st1np")
    assert ta1 is not None
    assert ta1.username == "kristinp"
    
    ta2 = StudentUser.authenticate("kristinp", "wrongpassword")
    assert ta2 is None
    
    
    ta4 = StudentUser.authenticate("kr1st1np", "kr1st1np")
    assert ta4 is None
    
    ta5 = StudentUser.authenticate("kristinp", "kristinp")
    assert ta5 is None
