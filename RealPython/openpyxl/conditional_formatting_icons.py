from openpyxl import load_workbook
from openpyxl.formatting.rule import IconSetRule


workbook = load_workbook("sample.xlsx")
sheet = workbook.active
icon_set_rule = IconSetRule("5Arrows", "num", [1, 2, 3, 4,  5])
sheet.conditional_formatting.add("H2:H100", icon_set_rule)
workbook.save(filename="sample_icon_set_rule.xlsx")
