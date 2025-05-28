from aiScript import queryAI
from openpyxl.utils import column_index_from_string
import os

def launchController(excelPath, wb, wsName, inColLetter, outColLetter, firstRow, lastRow):
    # print(f"Working on col {inColLetter} from rows {firstRow} to {lastRow}, outputting to col {outColLetter}, for worksheet {wsName} in {excelPath}")
    # print()

    baseFilename = os.path.basename(excelPath)
    filenameSansExt, ext = os.path.splitext(baseFilename)
    ws = wb[wsName]
    
    inColIndex = column_index_from_string(inColLetter)
    totalCharCountColIndex = inColIndex +1
    nameCharCountColIndex = inColIndex +2
    outColIndex = column_index_from_string(outColLetter)
    newNameCharCountColIndex = outColIndex +1
    differenceCharCountColIndex = outColIndex +2


    originalNamesList = []
    # IMPROPER: The max_row attribute of a worksheet does not take the column into account. Cannot get max row by worksheet column.
    for row in ws.iter_rows(min_row=firstRow, max_row=lastRow, min_col=inColIndex, max_col=inColIndex):
        originalNamesList.append(row[0].value)
    
    # print("Printing cellsList:")
    # print(cellsList)
    # print()

    newNamesList = queryAI(str(originalNamesList)).output_parsed

    i = 0
    for cellRow in range(firstRow, lastRow+1):
        # col B is already written and extracted
        # col C is already written
        ws.cell(row=cellRow, column=nameCharCountColIndex, value=len(originalNamesList[i])) # col D 
        ws.cell(row=cellRow, column=outColIndex, value=newNamesList.newFilenames[i]) # col E
        ws.cell(row=cellRow, column=newNameCharCountColIndex, value=len(newNamesList.newFilenames[i])) # col F
        ws.cell(row=cellRow, column=differenceCharCountColIndex, value= int(ws.cell(row=cellRow, column=totalCharCountColIndex).value) - len(originalNamesList[i]) + len(newNamesList.newFilenames[i])) # col G
        i += 1


    revisedFilename = f"{filenameSansExt}-Revised{ext}"
    wb.save(revisedFilename)
    os.startfile(revisedFilename)
    
    return
