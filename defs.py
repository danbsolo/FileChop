from procedureFunctions import *
from procedureClass import *


RESULTS_DIRECTORY = "File-Chop-Results"

EXCEED_CHARACTER_LIMIT_SUGGESTER = "File Rename Suggester (AI)"
FILE_NINJA_MODIFIER = "File-Ninja Modifier"
TYPO_FIXER = "Typo Fixer (AI)"


AI_PROCEDURES = {
    EXCEED_CHARACTER_LIMIT_SUGGESTER: Procedure(
        EXCEED_CHARACTER_LIMIT_SUGGESTER, 
        exceedCharacterLimitSuggesterFunction, 
        "pcFileRenamerPrompt.txt"),
    
    FILE_NINJA_MODIFIER: Procedure(
        FILE_NINJA_MODIFIER, 
        fileNinjaModifierFunction),
    
    TYPO_FIXER: Procedure(
        TYPO_FIXER, 
        typoFixerFunction, 
        "typoFixerPrompt.txt")
}

AI_PROCEDURES_DISPLAY = [
    FILE_NINJA_MODIFIER,
    TYPO_FIXER,
    EXCEED_CHARACTER_LIMIT_SUGGESTER,
]
