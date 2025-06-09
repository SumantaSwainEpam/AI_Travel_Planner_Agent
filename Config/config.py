#
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  

_model_cache = {}
_configured = False

def configure():
    global _configured
    if not _configured:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        genai.configure(api_key=api_key)
        _configured = True


def get_model(model_name="models/gemini-2.0-flash"):
    configure()
    if model_name not in _model_cache:
        _model_cache[model_name] = genai.GenerativeModel(model_name)
    return _model_cache[model_name]
