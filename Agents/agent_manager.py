# Agents/agent_manager.py
from Agents.budget_estimator import estimate_budget
from Agents.travel_planner import generate_itinerary
from Agents.map_linker import MapLinker
from Agents.pdf_exporter import generate_itinerary_pdf
from Agents.destination_images import get_destination_images

class AgentManager:
    def __init__(self):
        self.map = MapLinker

    def get_budget(self, dest, days):
        return estimate_budget(dest, days)

    def get_itinerary(self, dest, days):
        return generate_itinerary(dest, days)

    def get_map_url(self, place):
        return self.map.generate_search_url(place)

    def get_directions(self, from_loc, to_loc):
        return self.map.generate_directions_url(from_loc, to_loc)

    def export_itinerary_pdf(self, text, filename="itinerary.pdf"):
        return generate_itinerary_pdf(text, filename)
    
    def get_images(self, dest, count=3):
        return get_destination_images(dest, count)

