import folium
from src.algorithms.route_calculator import calculate_sea_route, get_port_coordinates

def create_map(start, end, get_port_coordinates):
    try:
        # Fetch the coordinates for the start and end ports
        start_coords = get_port_coordinates(start)
        end_coords = get_port_coordinates(end)

        if not start_coords or not end_coords:
            raise ValueError("Invalid start or end port coordinates")

        # Initialize a Folium map centered on the start port
        folium_map = folium.Map(location=start_coords, zoom_start=6)

        # Add markers for the start and end ports
        folium.Marker(location=start_coords, popup=f"Start: {start}", icon=folium.Icon(color="green")).add_to(folium_map)
        folium.Marker(location=end_coords, popup=f"End: {end}", icon=folium.Icon(color="red")).add_to(folium_map)

        # Calculate the sea route and get the route coordinates
        sea_route_info = calculate_sea_route(start, end)
        route_coords = sea_route_info.get("route_coords", [])

        if route_coords:
            # Add the route to the map as a polyline
            folium.PolyLine(route_coords, color="blue", weight=2.5, opacity=1).add_to(folium_map)
        else:
            folium_map = folium.Map(location=start_coords, zoom_start=6)
            folium.Marker(location=start_coords, popup="Invalid Route").add_to(folium_map)

        return folium_map

    except Exception as e:
        print(f"Error creating map: {str(e)}")
        return None

