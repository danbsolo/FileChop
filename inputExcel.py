import openpyxl as opxl
# import os

filename = "testExcel.xlsx" 
wb = opxl.Workbook()

ws0 = wb.active
ws0['A1'] = "i am a buterfliy"
ws0['A2'] = "nevr say nevr"
ws0['A3'] = "hi their fren"
ws0['A4'] = "not vry acesible"
ws0['A3'] = "im not enjying tht"


wb.save(filename)
wb.close()
