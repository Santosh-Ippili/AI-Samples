import os
from groq import Groq
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

api_key = os.getenv('GROQ_API_KEY')
# print(api_key)

groqClient = Groq(
    api_key=api_key,
)

# Chat history
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant specialized in providing information about Biryanis and More Restaurant in Toronto."
    }
]

while True:
    prompt = input("You: ")

    if prompt.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    # Add user message
    messages.append({"role": "user", "content": prompt})

    print("Assistant: Thinking...\n")

    # Call Groq
    response = groqClient.chat.completions.create(messages=messages, model="openai/gpt-oss-20b");
    #print(response)

    responseContent = response.choices[0].message.content

    # Print reply
    print("Assistant:", responseContent, "\n")

    # Save response
    messages.append({"role": "assistant", "content": responseContent})