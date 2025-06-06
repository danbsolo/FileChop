from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter
import os



def exceedCharacterLimitSuggesterFunction(inColIndex, outColIndex, firstRow, lastRow, inputList, outputList, ws):
    totalCharCountColIndex = inColIndex +1
    nameCharCountColIndex = inColIndex +2
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
    
    # write
    i = 0
    for cellRow in range(firstRow, lastRow+1):
        # col B is already written and extracted
        # col C is already written
        ws.cell(row=cellRow, column=nameCharCountColIndex, value=len(inputList[i])) # col D 
        ws.cell(row=cellRow, column=outColIndex, value=outputList.outputList[i]) # col E
        ws.cell(row=cellRow, column=newNameCharCountColIndex, value=len(outputList.outputList[i])) # col F
        ws.cell(row=cellRow, column=newTotalCharCountColIndex, value= int(ws.cell(row=cellRow, column=totalCharCountColIndex).value) - len(inputList[i]) + len(outputList.outputList[i])) # col G
        i += 1



def exceedCharacterLimitModifierFunction(inColIndex, outColIndex, firstRow, lastRow, inputList, outputList, ws):
    directoryColIndex = inColIndex -1
    # oldFilenameColIndex = inColIndex
    # newFilenameColIndex = outColIndex

    # define font stuff
    boldFont = Font(bold=True) # grayish
    successFill = PatternFill(fill_type="solid", fgColor="00FF80")
    failureFill = PatternFill(fill_type="solid", fgColor="FF4444")

    # get the first directory to be used    
    currentDirectory = ""
    i = firstRow
    while not currentDirectory:
        if (potentialDirectory := ws.cell(row=i, column=directoryColIndex).value):
            currentDirectory = potentialDirectory
        i -= 1

    # if oldFilenameCell and newFilenameCell are both not none and not identical, make the change
    for cellRow in range(firstRow, lastRow+1):
        # if we're on a new directory now, update currentDirectory
        if (potentialDirectory := ws.cell(row=cellRow, column=directoryColIndex).value):
            currentDirectory = potentialDirectory

        oldFilenameCell = ws.cell(row=cellRow, column=inColIndex)
        newFilenameCell = ws.cell(row=cellRow, column=outColIndex)

        if oldFilenameCell.value and newFilenameCell.value:
            try:
                os.rename(
                    f"{currentDirectory}\\{oldFilenameCell.value}",
                    f"{currentDirectory}\\{newFilenameCell.value}"
                )

                newFilenameCell.font = boldFont
                newFilenameCell.fill = successFill
                # print(f"Successfully renamed {oldFilename} to {newFilename}")

            except Exception as e:
                newFilenameCell.font = boldFont
                newFilenameCell.fill = failureFill
                # print(f"Error renaming {oldFilename} to {newFilename}: {e}")
        
        # write some sort of indicator the status of the rename in the new excel sheet

        


def typoFixerFunction(inColIndex, outColIndex, firstRow, lastRow, inputList, outputList, ws):
    # write
    i = 0
    for cellRow in range(firstRow, lastRow+1):
        ws.cell(row=cellRow, column=outColIndex, value=outputList.outputList[i])
        i += 1
