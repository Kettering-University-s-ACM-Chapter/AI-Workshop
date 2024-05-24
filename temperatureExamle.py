import os
import openai
from dotenv import load_dotenv
from openai import OpenAI


# Set the API key from the environment variable
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


# Setting up the conversation messages
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Who created the sun?"},
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    max_tokens=150,
    temperature=1.9
)

# Printing the output
# Access the correct attributes based on the response structure
print(response.choices[0].message)
