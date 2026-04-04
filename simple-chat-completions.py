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

response = groqClient.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Who is the president of India",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(response.choices[0].message.content)