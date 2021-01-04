import pandas as pd
from openpyxl import load_workbook
from mapping import REVIEW_ID

workbook = load_workbook(filename="sample.xlsx")
sheet = workbook.active

values = sheet.values

# Set the first row as the headers
cols = next(values)
data = list(values)

# Set index
idx = [row[REVIEW_ID] for row in data]

df = pd.DataFrame(data, index=idx, columns=cols)

print(df.head())
