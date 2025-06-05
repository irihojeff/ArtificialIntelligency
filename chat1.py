import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get OpenRouter API key instead
client = os.getenv("OPENROUTER_API_KEY")  # Change this

# Set system message
system_prompt = "You are a friendly and supportive teaching assistant for CS50. You are also a duck."

# Get user's question
user_prompt = input("What is your question? ")

# Use OpenRouter endpoint
url = "https://openrouter.ai/api/v1/chat/completions"  # Changed URL

headers = {
    "Authorization": f"Bearer {client}",
    "Content-Type": "application/json"
}

data = {
    "model": "deepseek/deepseek-chat:free",  # Free model
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
}

# Send request
response = requests.post(url, headers=headers, json=data)

# Handle response
if response.status_code == 200:
    answer = response.json()["choices"][0]["message"]["content"]
    print("\n🐥 Duck Assistant says:")
    print(answer)
else:
    print(f"Error {response.status_code}: {response.text}")