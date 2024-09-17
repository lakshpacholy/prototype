from geopy.distance import great_circle

# Example function to get maritime routes
def get_maritime_route(start_port, end_port):
    # Placeholder: Replace this with actual maritime route calculation logic
    return great_circle(get_port_coordinates(start_port), get_port_coordinates(end_port)).kilometers

# Define Indian ports with their coordinates
PORTS = {
    'Mumbai': (19.0760, 72.8777),
    'Chennai': (13.0827, 80.2707),
    'Kolkata': (22.5726, 88.3639),
    'Goa': (15.2993, 74.1240),
    'Delhi': (28.6139, 77.2090),
}

def get_port_coordinates(port_name):
    return PORTS.get(port_name)

def calculate_sea_route(start_port, end_port):
    route_distance = get_maritime_route(start_port, end_port)
    # Adjust the distance based on maritime data and constraints here
    return route_distance
