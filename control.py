from openpyxl.utils import column_index_from_string
import os
from defs import *
from aiScript import queryAI


def launchController(excelPath, wb, wsName, aiProcedureName, inColLetter, outColLetter, firstRow, lastRow):
    # set some variables
    baseFilename = os.path.basename(excelPath)
    filenameSansExt, ext = os.path.splitext(baseFilename)
    ws = wb[wsName]
    inColIndex = column_index_from_string(inColLetter)
    outColIndex = column_index_from_string(outColLetter)
    aiProcedureObject = AI_PROCEDURES[aiProcedureName]

    # row error handling
    if lastRow < firstRow:
        return

    # compile list of original input
    inputList = []
    for row in ws.iter_rows(min_row=firstRow, max_row=lastRow, min_col=inColIndex, max_col=inColIndex):
        inputList.append(row[0].value)

    ## prune both sides of inputList to not have None
    # prune from front
    while inputList and inputList[0] is None:
        inputList = inputList[1:]
        firstRow += 1
        break
    # prune from back
    while inputList and inputList[-1] is None:
        inputList = inputList[:-1]
        lastRow -= 1
    if not inputList:
        return

    # query AI (if a prompt was given)
    if aiProcedureObject.promptFile:
        with open(f"prompts/{aiProcedureObject.promptFile}", "r", encoding="utf-8") as f:
            developerInstructions = f.read()
        outputList = queryAI(str(inputList), developerInstructions).output_parsed
    else:
        outputList = None

    aiProcedureObject.mainFunction(inColIndex, outColIndex, firstRow, lastRow, inputList, outputList, ws)

    # Create RESULTS directory if it does not exist
    try: os.mkdir(RESULTS_DIRECTORY)
    except: pass
    
    # save the file and open
    revisedFilename = f"{RESULTS_DIRECTORY}\\{filenameSansExt}-Revised{ext}"
    wb.save(revisedFilename)
    os.startfile(revisedFilename)
    return 0
