from openpyxl import load_workbook
from openpyxl.drawing.image import Image


workbook = load_workbook(filename="hello_world.xlsx")
sheet = workbook.active

logo = Image("Engineers.jpg")
logo.height = 150
logo.width = 200

sheet.add_image(logo, "A3")
workbook.save(filename="hello_world_logo.xlsx")
