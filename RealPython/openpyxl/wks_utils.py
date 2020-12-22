from openpyxl import Workbook


def print_rows():
    for row in sheet.iter_rows(values_only=True):
        print(row)


workbook = Workbook()
sheet = workbook.active
