from openai import OpenAI
from pydantic import BaseModel
client = OpenAI()

class FilenameList(BaseModel):
    newFilenames: list[str]

def queryAI(userInput):
    with open("prompt.txt", "r", encoding="utf-8") as f:
        developerInstructions = f.read()

    response = client.responses.parse(
        model="gpt-4.1-nano",
        instructions=developerInstructions,
        input=userInput,
        text_format=FilenameList
    )

    return response

if __name__ == "__main__":
    userInput = input("Say something to the AI model: ")
    print()
    print(queryAI(userInput).output_text)