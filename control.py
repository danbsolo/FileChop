from aiScript import queryAI
from openpyxl.utils import column_index_from_string, get_column_letter
from openpyxl.styles import Font, PatternFill
import os

def launchController(excelPath, wb, wsName, inColLetter, outColLetter, firstRow, lastRow):
    """This code is very, VERY hard-coded to only work with the output from FileNinja's 'Exceed Character Limit' sheet."""

    # print(f"Working on col {inColLetter} from rows {firstRow} to {lastRow}, outputting to col {outColLetter}, for worksheet {wsName} in {excelPath}")
    # print()

    # set some variables
    baseFilename = os.path.basename(excelPath)
    filenameSansExt, ext = os.path.splitext(baseFilename)
    ws = wb[wsName]
    
    inColIndex = column_index_from_string(inColLetter)
    totalCharCountColIndex = inColIndex +1
    nameCharCountColIndex = inColIndex +2
    outColIndex = column_index_from_string(outColLetter)
    newNameCharCountColIndex = outColIndex +1
    newTotalCharCountColIndex = outColIndex +2


    # set headers
    headerFont = Font(bold=True) # grayish
    headerFill = PatternFill(fill_type="solid", fgColor="C0C0C0")
    
    def setHeader(colIndex, text):
        headerCell = ws.cell(row=1, column=colIndex, value=text)
        headerCell.font = headerFont
        headerCell.fill = headerFill
        ws.column_dimensions[get_column_letter(colIndex)].width = len(text) + 3

    setHeader(nameCharCountColIndex, "Total char count")
    setHeader(outColIndex, "Suggested new name")
    setHeader(newNameCharCountColIndex, "New name char count")
    setHeader(newTotalCharCountColIndex, "New total char count")


    # compile list of original filenames
    originalNamesList = []
    for row in ws.iter_rows(min_row=firstRow, max_row=lastRow, min_col=inColIndex, max_col=inColIndex):
        originalNamesList.append(row[0].value)
    
    # print("Printing cellsList:")
    # print(cellsList)
    # print()


    # query the AI based on original filenames
    with open("pcFileRenamerPrompt.txt", "r", encoding="utf-8") as f:
        developerInstructions = f.read()
    newNamesList = queryAI(str(originalNamesList), developerInstructions).output_parsed
    
    i = 0
    for cellRow in range(firstRow, lastRow+1):
        # col B is already written and extracted
        # col C is already written
        ws.cell(row=cellRow, column=nameCharCountColIndex, value=len(originalNamesList[i])) # col D 
        ws.cell(row=cellRow, column=outColIndex, value=newNamesList.newFilenames[i]) # col E
        ws.cell(row=cellRow, column=newNameCharCountColIndex, value=len(newNamesList.newFilenames[i])) # col F
        ws.cell(row=cellRow, column=newTotalCharCountColIndex, value= int(ws.cell(row=cellRow, column=totalCharCountColIndex).value) - len(originalNamesList[i]) + len(newNamesList.newFilenames[i])) # col G
        i += 1

    # save the file and open
    revisedFilename = f"{filenameSansExt}-Revised{ext}"
    wb.save(revisedFilename)
    os.startfile(revisedFilename)
    
    return
