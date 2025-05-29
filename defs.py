from aiProcedureFunctions import *
from aiProcedureClass import *

EXCEED_CHARACTER_LIMIT = "Exceed Character Limit"
TYPO_FIXER = "Typo Fixer"

AI_PROCEDURES = {
    EXCEED_CHARACTER_LIMIT: AI_Procedure_Class(EXCEED_CHARACTER_LIMIT, exceedCharacterLimitFunction, "pcFileRenamerPrompt.txt") ,
    TYPO_FIXER: AI_Procedure_Class(TYPO_FIXER, typoFixerFunction, "typoFixerPrompt.txt")
}

AI_PROCEDURES_DISPLAY = [
    EXCEED_CHARACTER_LIMIT,
    TYPO_FIXER
]