from openai import OpenAI
client = OpenAI()


text = input("Say something to the AI model.:\n")
print()


response = client.responses.create(
    model="gpt-4.1-nano",
    instructions="You'll be given the name of a file related to Parks Canada. Shorten it as best you can and fix any typos. Words must be separated by hyphens. First letter of each word must be capitalized.",
    input=text
)


print(response.output_text)