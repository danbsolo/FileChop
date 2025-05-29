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

    # compile list of original input
    inputList = []
    for row in ws.iter_rows(min_row=firstRow, max_row=lastRow, min_col=inColIndex, max_col=inColIndex):
        inputList.append(row[0].value)

    # query AI
    with open(f"prompts/{aiProcedureObject.promptFile}", "r", encoding="utf-8") as f:
        developerInstructions = f.read()
    outputList = queryAI(str(inputList), developerInstructions).output_parsed

    aiProcedureObject.mainFunction(inColIndex, outColIndex, firstRow, lastRow, inputList, outputList, ws)

    # save the file and open
    revisedFilename = f"{filenameSansExt}-Revised{ext}"
    wb.save(revisedFilename)
    os.startfile(revisedFilename)
    return 0
