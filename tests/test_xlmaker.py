"""Test module for the xlmaker module"""
import os
import pytest
from XL2Cal import xlmaker

VALID_NAMES = ["test1", " test 3", "Hello Excel"]
INVALID_NAMES = ["test.xlsx", "test stuff.csv", ".test."]


def teardown_module():
    """Tears down any files that were created"""
    for name in VALID_NAMES:
        if os.path.isfile(name + ".xlsx"):
            os.remove(name + ".xlsx")

    for name in INVALID_NAMES:
        if os.path.isfile(name + ".xlsx"):
            os.remove(name + ".xlsx")

def test_names_with_periods():
    """tests that names with periods are invalid"""
    with pytest.raises(NameError):
        for invalid in INVALID_NAMES:
            xlmaker.valid_name(invalid)

def test_valid_names():
    """tests that valid names are indeed marked as valid"""
    for valid in VALID_NAMES:
        assert xlmaker.valid_name(valid) is True

def test_make_valid_name():
    """tests that an excel document is created with the correct format"""
    from openpyxl import Workbook
    xlmaker.make(VALID_NAMES[0])
    assert os.path.isfile(VALID_NAMES[0] + ".xlsx")

def test_make_invalid_name():
    """tests that file is not created if invalid name provided"""
    xlmaker.make(INVALID_NAMES[0])
    assert os.path.isfile(INVALID_NAMES[0] + ".xlsx") is False

def test_make_correct_format():
    """Tests that the document that is created has the correct format"""
    pass