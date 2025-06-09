# Agents/destination_images.py
import google.generativeai as genai
from Config.config import get_model

model= get_model()
def get_destination_images(place: str, count: int = 3) -> list[str]:
    prompt = (
        f"Give me {count} royalty-free image URLs that represent popular tourist attractions or scenic views in {place}. "
        "Ensure URLs are publicly accessible."
    )
    response = model.generate_content(prompt)
    # Simple extraction — assumes Gemini responds with clean URLs
    urls = [line.strip() for line in response.text.split('\n') if line.startswith("http")]
    return urls[:count]
