import folium

def create_map(start_port, end_port, get_port_coordinates):
    start_coords = get_port_coordinates(start_port)
    end_coords = get_port_coordinates(end_port)
    
    if not start_coords or not end_coords:
        raise ValueError("Invalid ports specified")
    
    # Initialize the map
    m = folium.Map(location=[(start_coords[0] + end_coords[0]) / 2, (start_coords[1] + end_coords[1]) / 2], zoom_start=5)
    
    # Add markers for ports
    folium.Marker(start_coords, popup=f"Start: {start_port}").add_to(m)
    folium.Marker(end_coords, popup=f"End: {end_port}").add_to(m)
    
    # Add a line between ports
    folium.PolyLine([start_coords, end_coords], color='blue', weight=2.5, opacity=1).add_to(m)
    
    return m
