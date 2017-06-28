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
    worksheet = workbook.active
    worksheet.title = "Events List"
    worksheet['A1'] = "Event Name"
    worksheet['B1'] = "Event Start Date"
    worksheet['C1'] = "Event Start Time"
    worksheet['D1'] = "Event End Date"
    worksheet['E1'] = "Event End Time"
    worksheet.column_dimensions['A'].width = 20
    try:
        if valid_name(file_name):
            workbook.save(file_name + ".xlsx")
    except NameError as name_error:
        print str(name_error)

def valid_name(file_name):
    """determines that that the passed file_name
    is valid, mainly making sure that it contains
    no periods to prevent extension issues
    """
    if '.' in file_name:
        raise NameError("Name must not contain periods")
    else:
        return True
