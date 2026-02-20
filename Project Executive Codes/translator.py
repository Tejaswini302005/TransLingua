import os
from google import genai
from dotenv import load_dotenv

# Load API key
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Create client
client = genai.Client(api_key=API_KEY)


def translate_text(text, source_lang, target_lang):

    prompt = f"""
Translate the following text from {source_lang} to {target_lang}:

{text}

Only give translated text.
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text
