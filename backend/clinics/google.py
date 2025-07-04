import requests

def get_nearby_clinics(lat, lon, radius=3000):
    endpoint = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": f"{lat},{lon}",
        "radius": radius,
        "type": "hospital",
        "key": "YOUR_GOOGLE_API_KEY"
    }
    response = requests.get(endpoint, params=params)
    return response.json()
