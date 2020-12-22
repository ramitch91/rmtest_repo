from openpyxl import Workbook


def print_rows():
    for rows in sheet.iter_rows(values_only=True):
        print(rows)


workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "hello"
sheet["B1"] = "world"
print_rows()
print()

sheet.insert_cols(idx=1)
print_rows()
print()

sheet.insert_cols(idx=3, amount=5)
print_rows()
print()

sheet.delete_cols(idx=3, amount=5)
sheet.delete_cols(idx=1)
print_rows()
print()

sheet.insert_rows(idx=1)
print_rows()
print()

sheet.insert_rows(idx=1, amount=3)
print_rows()
print()

sheet.delete_rows(idx=1, amount=4)
print_rows()
print()

sheet["B10"] = "test"
print_rows()

workbook.save(filename="hello_world.xlsx")
