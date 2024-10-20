import sys
import os
import pytest
from unittest import mock

# Adding the project root directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Correct import for app_administrator
from app.app_administrator import AdministratorUser

@pytest.fixture
def mock_read_file():
    return [
        "A001;Lilo;Stitch;1990-05-05;1234567890;lilo@example.com;lilo;l1l0",
        "A002;Invce;Smith;1985-08-12;0987654321;invce@example.com;invce;invc3"
    ]

@mock.patch("app.app_administrator.util.read_file")
def test_authenticate(mock_read_file_function, mock_read_file):
    mock_read_file_function.return_value = mock_read_file

    ta1 = AdministratorUser.authenticate("lilo", "l1l0")
    assert ta1 is not None
    assert ta1.username == "lilo"
    
    ta2 = AdministratorUser.authenticate("lilo", "wrongpassword")
    assert ta2 is None
    
    ta3 = AdministratorUser.authenticate("invce", "invc3")
    assert ta3 is not None
    assert ta3.username == "invce"
    
    ta4 = AdministratorUser.authenticate("invce", "wrongpassword")
    assert ta4 is None
    
    ta5 = AdministratorUser.authenticate("nonexistent", "password")
    assert ta5 is None
