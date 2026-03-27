import anthropic
from dotenv import load_dotenv
import os

# Load the API key from .env file
load_dotenv()

# Create the Anthropic client
# It automatically reads ANTHROPIC_API_KEY from the environment
client = anthropic.Anthropic()

# Send a message to Claude
message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is IFRS17 in one sentence?"}
    ]
)

# Print the response
print(message.content[0].text)
