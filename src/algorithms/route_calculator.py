import requests
from geopy.distance import great_circle

PORTS = {
    'Mumbai': (18.9253, 72.8438),
    'Chennai': (13.0827, 80.2707),
    'Kolkata': (22.5726, 88.3639),
    'Goa': (15.2993, 74.1240),
    'Delhi': (28.6139, 77.2090),
    'Dighi Port': (18.2777, 72.9686)
}

API_KEY = 'uzFYoLlMoZ6i3cBiqlHY5snTkrlL1CnMPkBZHZ50'

def get_port_coordinates(port_name):
    return PORTS.get(port_name)

def fetch_searoutes_api(start_lat, start_lon, end_lat, end_lon):
    url = f"https://api.searoutes.com/route/v2/sea/{start_lon},{start_lat};{end_lon},{end_lat}?continuousCoordinates=true&allowIceAreas=false&avoidHRA=false&avoidSeca=false"
    headers = {
        "accept": "application/json",
        "x-api-key": API_KEY
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching SeaRoutes API: {response.status_code}, {response.text}")

def calculate_sea_route(start_port, end_port):
    try:
        start_coords = get_port_coordinates(start_port)
        end_coords = get_port_coordinates(end_port)
        
        if not start_coords or not end_coords:
            return {"error": "Invalid port name(s)"}
        
        route_info = fetch_searoutes_api(start_coords[0], start_coords[1], end_coords[0], end_coords[1])
        
        # Extract coordinates for the route path
        features = route_info.get('features', [])
        if not features:
            return {"error": "No route data found in API response"}
        
        route_coords = features[0]['geometry']['coordinates']
        
        # Convert route coordinates to [lat, lon] format for Folium
        route_coords = [[lat, lon] for lon, lat in route_coords]
        
        return {
            "route_coords": route_coords,
            "direct_distance_km": great_circle(start_coords, end_coords).kilometers
        }
    except Exception as e:
        return {"error": str(e)}
