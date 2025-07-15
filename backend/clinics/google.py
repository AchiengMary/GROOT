import requests

def get_nearby_clinics(lat: float, lon: float, api_key: str, radius=3000):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lon}",
        "radius": radius,
        "type": "hospital",
        "key": api_key
    }
    res = requests.get(url, params=params)
    return res.json().get("results", [])