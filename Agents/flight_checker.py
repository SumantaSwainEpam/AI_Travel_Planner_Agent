import google.generativeai as genai
from Config.config import get_model

def check_flight_cost(source, destination, travel_date):
    prompt = (
        f"Give an approximate flight cost from {source} to {destination} "
        f"for the date {travel_date}. Mention airline options and typical price range in INR."
    )
    model = get_model()
    response = model.generate_content(prompt)
    return response.text
