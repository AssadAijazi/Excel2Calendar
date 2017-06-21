"""Module for creating excel documents that are used as
the input for the program. Users can use an excel document
generated from this module to enter in information for
various calendar events. The excel document will then be
loaded back in to the software and added to the user's
google calendar.
"""

from openpyxl import Workbook

def make(file_name):
    """generate an excel document that can be used
    enter data for multiple calendar events.

    @params: file_name: The name of the excel document to be created
    @return: none (creates new file)
    """
    workbook = Workbook()
    workbook.save(file_name)
