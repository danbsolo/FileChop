from openai import OpenAI
client = OpenAI()

def queryAI(userInput):
    with open("prompt.txt", "r", encoding="utf-8") as f:
        developerInstructions = f.read()

    response = client.responses.create(
        model="gpt-4.1-nano",
        instructions=developerInstructions,
        input=userInput
    )

    return response

if __name__ == "__main__":
    userInput = input("Say something to the AI model: ")
    print()
    print(queryAI(userInput).output_text)