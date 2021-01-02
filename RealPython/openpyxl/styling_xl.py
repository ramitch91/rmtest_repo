from openpyxl import load_workbook
from openpyxl.styles import (
    Font,
    Color,
    colors,
    Alignment,
    Side,
    Border,
)
from openpyxl.styles import NamedStyle

workbook = load_workbook(filename="sample.xlsx")
sheet = workbook.active
bold_font = Font(bold=True)
big_blue_text = Font(color=colors.BLUE, size=20)
center_aligned_text = Alignment(horizontal="center")
double_border_side = Side(border_style="double")
square_border = Border(top=double_border_side,
                       right=double_border_side,
                       bottom=double_border_side,
                       left=double_border_side)

sheet["A2"].font = bold_font
sheet["A3"].font = big_blue_text
sheet["A4"].alignment = center_aligned_text
sheet["A5"].border = square_border

header = NamedStyle(name="header")
header.font = Font(bold=True)
header.border = Border(bottom=Side(border_style="thin"))
header.alignment = Alignment(horizontal="center", vertical="center")
header_row = sheet[1]
for cell in header_row:
    cell.style = header

workbook.save(filename="sample_styles.xlsx")
