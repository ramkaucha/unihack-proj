import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = OPEN_API

def detect_language(text):
    """Detects language from user input."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Detect language of this text."},
                  {"role": "user", "content": text}]
    )
    return response["choices"][0]["message"]["content"].strip()

def generate_issue_report(conversation_history, language):
    """Generates structured report from conversation."""
    full_input = "\n".join(conversation_history)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": f"Create structured issue report in {language}."},
                  {"role": "user", "content": full_input}]
    )
    return response["choices"][0]["message"]["content"].strip()
