# Insurance Product Explainer Chatbot

## What This Project Does
A conversational chatbot that answers questions about insurance products.
Built with Python, the Anthropic Claude API, and Streamlit.

## Stack
- Python 3.11
- Anthropic Python SDK (claude-3-5-sonnet)
- Streamlit (browser UI)
- python-dotenv (API key management)

## How to Run
1. Add your Anthropic API key to .env: ANTHROPIC_API_KEY=your_key_here
2. Install dependencies: pip install -r requirements.txt
3. Launch the app: streamlit run src/chatbot.py

## Project Structure
- src/chatbot.py       Main application
- .env                 API key (never commit this)
- requirements.txt     Python dependencies
- CLAUDE.md            This file

## Conventions
- One file per stage until the project is complete
- Commit at the end of each stage with a clear message
