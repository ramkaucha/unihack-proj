import os
import openai

# Load OpenAI API key securely from environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Missing OpenAI API key. Please set the OPENAI_API_KEY environment variable.")
openai.api_key = api_key

def detect_language(text):
    """Detects the language of the input text."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a language detection assistant."},
            {"role": "user", "content": f"Detect the language of this text and respond only with the language name:\n\n{text}"}
        ],
        temperature=0
    )
    return response["choices"][0]["message"]["content"].strip()

def check_for_inappropriate_content(text):
    """Detects inappropriate content."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Analyze the text for violence, hate speech, or sexual harassment. Respond with 'safe' or 'inappropriate'."},
            {"role": "user", "content": text}
        ],
        temperature=0
    )
    return response["choices"][0]["message"]["content"].strip().lower()

def generate_issue_report(text, language):
    """Generates a structured issue report."""
    prompt = f"""
    Convert the following user input into a structured issue report in {language}:
    {text}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You structure user issues into detailed reports for developers."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"].strip()

def translate_to_english(text):
    """Translates the report into English."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Translate this issue report into English."},
            {"role": "user", "content": text}
        ],
        temperature=0.3
    )
    return response["choices"][0]["message"]["content"].strip()
