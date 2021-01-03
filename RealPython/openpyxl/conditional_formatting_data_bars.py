from openpyxl import load_workbook
from openpyxl.styles import colors
from openpyxl.formatting.rule import DataBarRule


workbook = load_workbook("sample.xlsx")
sheet = workbook.active
data_bar_rule = DataBarRule(start_type="num",
                            start_value=1,
                            end_type="num",
                            end_value=5,
                            color=colors.GREEN)
sheet.conditional_formatting.add("H2:H100", data_bar_rule)
workbook.save(filename="sample_data_bar_rule.xlsx")
