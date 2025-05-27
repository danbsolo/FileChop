from queryAI import queryAI
from openpyxl.utils import column_index_from_string
import os

def start(excelPath, wb, wsName, inColLetter, outColLetter, firstRow, lastRow):
    print(f"Working on col {inColLetter} from rows {firstRow} to {lastRow}, outputting to col {outColLetter}, for worksheet {wsName} in {excelPath}")
    print()

    filenameSansExt, ext = os.path.splitext(excelPath)
    ws = wb[wsName]
    inColIndex = column_index_from_string(inColLetter)
    outColIndex = column_index_from_string(outColLetter)

    cellsList = []
    # IMPROPER: The max_row attribute of a worksheet does not take the column into account. Cannot get max row by worksheet column.
    for row in ws.iter_rows(min_row=firstRow, max_row=lastRow, min_col=inColIndex, max_col=inColIndex):
        cellsList.append(row[0].value)
        # rowValue = row[0].value
        # if not rowValue: print()
        # else: print(rowValue)
    
    print("Printing cellsList:")
    print(cellsList)
    print()

    paragraphList = queryAI(str(cellsList)).output_parsed

    i = 0
    for cellRow in range(firstRow, lastRow+1):
        ws.cell(row=cellRow, column=outColIndex, value=paragraphList.correctedParagraphs[i])
        i += 1


    revisedFilename = f"{filenameSansExt}-Revised{ext}"
    wb.save(revisedFilename)
    os.startfile(revisedFilename)
    
    return

