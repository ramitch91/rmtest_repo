from openpyxl import load_workbook
from openpyxl.utils import FORMULAE

workbook = load_workbook("sample_formulas.xlsx")
sheet = workbook.active
sheet["P2"] = "=AVERAGE(H2:H100)"
sheet["P3"] = '=COUNTIF(I2:I100, ">0")'
workbook.save(filename="sample_formulas.xlsx")
