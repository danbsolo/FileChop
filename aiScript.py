from openai import OpenAI
client = OpenAI()


def queryAI(userInput):
    response = client.responses.create(
        model="gpt-4.1-nano",
        instructions="Insert an NBA analogy into any response you give.",
        input=userInput
    )

    return response.output_text


if __name__ == "__main__":
    text = input("Say something to the AI model.: ")
    print()
    print(queryAI(text))