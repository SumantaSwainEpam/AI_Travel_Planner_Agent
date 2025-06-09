
from Config.config import get_model

def estimate_budget(destination, days):
    model=get_model()
    prompt = (
        f"Estimate a budget for a {days}-day trip to {destination}. "
        "Include approx cost of flights, hotel, food, local travel, and buffer."
    )
    response = model.generate_content(prompt)
    return response.text
