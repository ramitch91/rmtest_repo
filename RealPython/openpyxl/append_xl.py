from openpyxl import load_workbook

# Open the spreadsheet and select the main sheet
workbook = load_workbook(filename="hello_world.xlsx")
sheet = workbook.active

# Write into a specific cell
sheet["C1"] = "writing ;)"

# Save the spreadsheet
workbook.save(filename="hello_world_append.xlsx")