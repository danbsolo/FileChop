from openai import OpenAI
client = OpenAI()


def queryAI(userInput):
    response = client.responses.create(
        model="gpt-4.1",
        input=userInput
    )

    return response


if __name__ == "__main__":
    text = input("Say something to the AI model: ")
    print()
    response = queryAI(text)
    print(response.output_text)