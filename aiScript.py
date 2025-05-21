from openai import OpenAI
client = OpenAI()


def queryAI(userInput):
    response = client.responses.create(
        model="gpt-4.1-nano",
        instructions="You'll be given a Python list. Return a comma separated list of the values in the same order after making the following changes: Fix any typos. (Lack of apostrophe may be a typo). Words must be separated by hyphens. First letter of each word must be capitalized.",
        input=userInput
    )

    return response.output_text


if __name__ == "__main__":
    text = input("Say something to the AI model.:\n")
    print()