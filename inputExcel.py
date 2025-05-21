import openpyxl as opxl
from tkinter.filedialog import askopenfilename
# import os

filename = askopenfilename(filetypes=[("Excel files", ".xlsx")])
wb = opxl.Workbook()

ws0 = wb.active
ws0['A1'] = "i am a buterfliy"
ws0['A2'] = "nevr say nevr"
ws0['A3'] = "hi their fren"
ws0['A4'] = "not vry acesible"
ws0['A5'] = "im not enjying tht"

wb.save(filename)
wb.close()
