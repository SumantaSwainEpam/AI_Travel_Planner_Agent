import google.generativeai as genai
from dotenv import load_dotenv
from Config.config import get_model
load_dotenv()

def generate_itinerary(place: str, days: int) -> str:
   
    model=get_model()
    prompt = (
        f"You're a helpful travel planner. Create a {days}-day travel itinerary "
        f"for a trip to {place}. Include top attractions, food, and tips."
    )
    response = model.generate_content(prompt)
    return response.text
