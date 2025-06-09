from Config.config import configure
from Agents.travel_planner import generate_itinerary

configure()

print("Welcome to Travel Planner AI")
destination = input("Enter your destination: ")
days = input("Number of days: ")

try:
    days = int(days)
    print("\n Your Itinerary:\n")
    itinerary = generate_itinerary(destination, days)
    print(itinerary)
except ValueError:
    print(" Please enter a valid number for days.")
