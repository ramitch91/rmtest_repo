from openpyxl import load_workbook
from openpyxl.styles import colors
from openpyxl.formatting.rule import ColorScaleRule


workbook = load_workbook("sample.xlsx")
sheet = workbook.active
color_scale_rule = ColorScaleRule(start_type="min",
                                  start_color=colors.RED,
                                  end_type="max",
                                  end_color=colors.GREEN)
sheet.conditional_formatting.add("H2:H100", color_scale_rule)
workbook.save(filename="sample_color_scale_rule.xlsx")
