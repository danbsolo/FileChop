from openai import OpenAI
client = OpenAI()


def queryAI(userInput):
    response = client.responses.create(
        model="gpt-4.1-nano",
        instructions="You'll be given a Python list. Return a comma separated list of the values in the same order after fix any typos (including lack of apostrophe if applicable), and capitalize the first letter of each word.",
        input=userInput
    )

    return response.output_text


if __name__ == "__main__":
    text = input("Say something to the AI model.:\n")
    print()