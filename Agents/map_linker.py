
import urllib.parse
class MapLinker:
    @staticmethod
    def generate_search_url(destination: str) -> str:
        """Search for a place on Google Maps."""
        query = urllib.parse.quote_plus(destination)
        return f"https://www.google.com/maps/search/?api=1&query={query}"

    @staticmethod
    def generate_directions_url(origin: str, destination: str, travel_mode: str = "driving") -> str:
        """Generate directions from origin to destination."""
        origin = urllib.parse.quote_plus(origin)
        destination = urllib.parse.quote_plus(destination)
        return f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}&travelmode={travel_mode}"

    @staticmethod
    def generate_place_details_url(place_id: str) -> str:
        """Link to a specific place using Place ID (needs Google Maps API support)."""
        return f"https://www.google.com/maps/place/?q=place_id:{place_id}"

    @staticmethod
    def generate_latlng_pin_url(lat: float, lng: float) -> str:
        """Pin specific lat/lng coordinates."""
        return f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
