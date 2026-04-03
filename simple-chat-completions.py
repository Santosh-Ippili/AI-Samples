import os
from groq import Groq
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

api_key = os.getenv('GROQ_API_KEY')
# print(api_key)

client = Groq(
    api_key=api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Who is the president of India",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)