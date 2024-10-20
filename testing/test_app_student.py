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
        "s0002;gjdfhg;fgdfg;01/01/2001;7777777777;jfdgf;gdf;dfg;['AI', 'PyLearn'];[0, 0, 0, 0, 0, 0]",
        "s0003;sdfdsfadsf;dsfdsfdsfds;10/10/2000;1111111111;111;qwe;qwe;['AI'];[0, 0, 0, 0, 0, 0]",
        "s0004;fsdfsd;sdfdsf;20/02/2020;6666666666;fdf;54345;34534;['AI', 'PyLearn'];[0, 0, 0, 0, 0, 0]"
    ]

@mock.patch("app.app_administrator.util.read_file")
def test_authenticate(mock_read_file_function, mock_read_file):
    mock_read_file_function.return_value = mock_read_file

    ta1 = StudentUser.authenticate("kristinp", "kr1st1np")
    assert ta1 is not None
    assert ta1.username == "kristinp"
    
    ta2 = StudentUser.authenticate("kristinp", "wrongpassword")
    assert ta2 is None
    
    ta3 = StudentUser.authenticate("gdf", "dfg")
    assert ta3 is not None
    assert ta3.username == "gdf"
    
    ta4 = StudentUser.authenticate("gdf", "kr1st1np")
    assert ta4 is None
    
    ta5 = StudentUser.authenticate("kristinp", "dfg")
    assert ta5 is None
