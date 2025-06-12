from procedureFunctions import *
from procedureClass import *


RESULTS_DIRECTORY = "File-Chop-Results"

FILE_RENAME_SUGGESTER = "File Rename Suggester (AI)"
FILE_NINJA_MODIFIER = "File-Ninja Modifier"
TYPO_FIXER = "Typo Fixer (AI)"


AI_PROCEDURES = {
    FILE_RENAME_SUGGESTER: Procedure(
        FILE_RENAME_SUGGESTER, 
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
    FILE_RENAME_SUGGESTER,
    FILE_NINJA_MODIFIER,
    TYPO_FIXER,
]
