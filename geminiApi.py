
import os

from dotenv import load_dotenv
#python3.12 -m pip install python-dotenv

from google import genai
#python3.12 -m pip install google-genai

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=api_key)

# 1) Create a persistent chat
chat = client.chats.create(
    model="gemini-2.5-flash"
)

# 2) Send messages on the same chat object
response = chat.send_message("Explain how AI works in a few words")
print(response.text)

# 3) Send another message; it keeps context
response = chat.send_message("Can you make it even shorter?")
print(response.text)
