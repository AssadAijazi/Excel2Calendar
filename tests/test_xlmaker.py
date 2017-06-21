"""Test module for the xlmaker module"""
import os
import pytest
from XL2Cal import xlmaker

NAMES = {"valid": "test", "invalid": "te.st"}

def teardown_module():
    """Tears down any files that were created"""
    for name in NAMES.values():
        if os.path.isfile(name + ".xlsx"):
            os.remove(name + ".xlsx")

def test_make():
    """tests that an excel documents can be created"""
    xlmaker.make(NAMES["valid"])
    assert os.path.isfile(NAMES["valid"] + ".xlsx")

def test_make_invalid():
    """tests that file is not created if invalid name provided"""
    xlmaker.make(NAMES["invalid"])
    assert os.path.isfile(NAMES["invalid"] + ".xlsx") is False

def test_names_with_periods():
    """tests that names with periods are invalid"""
    with pytest.raises(NameError):
        xlmaker.valid_name("test.xlsx")
        xlmaker.valid_name("te.st.txt")
        xlmaker.valid_name("Test . test ")

def test_valid_names():
    """tests that valid names are indeed marked as valid"""
    assert xlmaker.valid_name("test") is True
    assert xlmaker.valid_name("Valid name") is True
