import folium
from src.algorithms.route_calculator import calculate_sea_route, get_port_coordinates

def create_map(start, end, get_coordinates_func):
    start_coords = get_coordinates_func(start)
    end_coords = get_coordinates_func(end)
    
    if not start_coords or not end_coords:
        raise ValueError("Invalid start or end port coordinates")

    route_info = calculate_sea_route(start, end)
    route_coords = route_info.get("route_coords", [])
    
    print("Route Coordinates:", route_coords)  # Add this line
    
    # Convert the coordinates to [lat, lon] format for Folium
    route_coords = [[lat, lon] for lon, lat in route_coords]
    
    m = folium.Map(location=[(start_coords[0] + end_coords[0]) / 2, (start_coords[1] + end_coords[1]) / 2], zoom_start=5)
    
    # Add start and end markers
    folium.Marker(location=start_coords, popup=f"Start: {start}", icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(location=end_coords, popup=f"End: {end}", icon=folium.Icon(color='red')).add_to(m)
    
    # Add route line if coordinates are available
    if route_coords:
        folium.PolyLine(locations=route_coords, color='blue').add_to(m)
    else:
        print("No route coordinates available to display on the map.")
    
    return m
