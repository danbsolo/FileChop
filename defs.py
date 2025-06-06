from procedureFunctions import *
from procedureClass import *


RESULTS_DIRECTORY = "File-Chop-Results"


EXCEED_CHARACTER_LIMIT_SUGGESTER = "Exceed Character Limit Suggester (AI)"
EXCEED_CHARACTER_LIMIT_MODIFIER = "Exceed Character Limit Modifier"
TYPO_FIXER = "Typo Fixer (AI)"


AI_PROCEDURES = {
    EXCEED_CHARACTER_LIMIT_SUGGESTER: Procedure(
        EXCEED_CHARACTER_LIMIT_SUGGESTER, 
        exceedCharacterLimitSuggesterFunction, 
        "pcFileRenamerPrompt.txt"),
    
    EXCEED_CHARACTER_LIMIT_MODIFIER: Procedure(
        EXCEED_CHARACTER_LIMIT_MODIFIER, 
        exceedCharacterLimitModifierFunction),
    
    TYPO_FIXER: Procedure(
        TYPO_FIXER, 
        typoFixerFunction, 
        "typoFixerPrompt.txt")
}

AI_PROCEDURES_DISPLAY = [
    EXCEED_CHARACTER_LIMIT_MODIFIER,
    TYPO_FIXER,
    EXCEED_CHARACTER_LIMIT_SUGGESTER,
]
