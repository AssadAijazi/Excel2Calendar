"""Test module for the xlmaker module"""
import os
from XL2Cal import xlmaker

def teardown_module():
    """Tears down any files that were created"""
    if os.path.isfile("test.xlsx"):
        os.remove("test.xlsx")

def test_make():
    """tests that an excel documents can be created"""
    xlmaker.make("test.xlsx")
    assert os.path.isfile("test.xlsx")
