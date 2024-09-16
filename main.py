import json
import argparse
import folium
import plotly.graph_objects as go
import networkx as nx
import math
import webbrowser
import os

# Import NOAA data fetch functions from noaa_data_fetcher.py
from noaa_data_fetcher import fetch_weather_data, fetch_ocean_data

def load_nodes(filename):
    """
    Load the generated valid nodes from a JSON file.
    """
    try:
        with open(filename, 'r') as file:
            nodes = json.load(file)
        return nodes
    except Exception as e:
        print(f"Error loading nodes: {e}")
        return None

def haversine_distance(coord1, coord2):
    """
    Calculate the Haversine distance between two geographic coordinates.
    """
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    R = 6371  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

def adjust_weight_with_noaa_data(distance, weather_data, ocean_data, coord1, coord2):
    """
    Adjust the edge weight (distance) based on weather and ocean conditions.
    """
    wind_speed = weather_data.get('wind_speed', 10)  # Default to 10 knots if not available
    wave_height = weather_data.get('wave_height', 2)  # Default to 2 meters if not available
    current_speed = ocean_data.get('current_speed', 1)  # Default to 1 knot if not available

    # Simple model: Increase distance based on adverse conditions
    wind_factor = 1 + (wind_speed / 50)  # Assuming wind_speed ranges from 0 to 50 knots
    wave_factor = 1 + (wave_height / 10)  # Assuming wave_height ranges from 0 to 10 meters
    current_factor = 1 - (current_speed / 10)  # Favorable currents reduce travel time

    # Ensure current_factor doesn't go negative
    current_factor = max(current_factor, 0.5)

    # Combine factors to adjust the weight
    adjusted_distance = distance * wind_factor * wave_factor * current_factor

    # Handle storm warnings
    if weather_data.get('storm_warning', False):
        adjusted_distance *= 2  # Penalize heavily if there's a storm warning

    return adjusted_distance

def find_optimal_route(nodes, start_node, end_node, weather_data, ocean_data):
    """
    Find the optimal route using Dijkstra's algorithm, considering NOAA data.
    """
    G = nx.Graph()
    
    # Add nodes to the graph
    for node, coords in nodes.items():
        G.add_node(node, pos=coords)
    
    # Add edges with weights adjusted for weather and ocean data
    for node1, coords1 in nodes.items():
        for node2, coords2 in nodes.items():
            if node1 != node2:
                distance = haversine_distance(coords1, coords2)
                
                # Adjust distance based on NOAA data
                adjusted_weight = adjust_weight_with_noaa_data(distance, weather_data, ocean_data, coords1, coords2)
                
                G.add_edge(node1, node2, weight=adjusted_weight)
    
    # Find shortest path
    try:
        path = nx.shortest_path(G, source=start_node, target=end_node, weight='weight')
    except nx.NetworkXNoPath:
        print("No path found.")
        return []
    
    return path

def visualize_route_on_map(route, nodes, map_filename):
    """
    Visualize the route on a Folium map and save it as an HTML file.
    """
    start_coords = nodes[route[0]]
    end_coords = nodes[route[-1]]
    midpoint = [(start_coords[0] + end_coords[0]) / 2, (start_coords[1] + end_coords[1]) / 2]
    
    m = folium.Map(location=midpoint, zoom_start=6)
    
    # Add markers for start and end nodes
    folium.Marker(location=start_coords, popup='Start', icon=folium.Icon(color='green')).add_to(m)
    folium.Marker(location=end_coords, popup='End', icon=folium.Icon(color='red')).add_to(m)
    
    # Add route line
    route_coords = [nodes[node] for node in route]
    folium.PolyLine(locations=route_coords, color='blue', weight=2.5, opacity=0.7).add_to(m)
    
    m.save(map_filename)
    print(f"Folium map saved to {map_filename}")

def visualize_route_on_plotly(route, nodes, plotly_filename):
    """
    Visualize the route using Plotly and save it as an HTML file.
    """
    edge_x = []
    edge_y = []
    for i in range(len(route) - 1):
        x0, y0 = nodes[route[i]]
        x1, y1 = nodes[route[i + 1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    node_x = [coords[1] for coords in nodes.values()]
    node_y = [coords[0] for coords in nodes.values()]

    edge_trace = go.Scattergeo(
        lon=edge_x,
        lat=edge_y,
        mode='lines',
        line=dict(width=2, color='blue'),
        name='Route'
    )

    node_trace = go.Scattergeo(
        lon=node_x,
        lat=node_y,
        mode='markers',
        marker=dict(size=6, color='red'),
        text=[node for node in nodes],
        hoverinfo='text'
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='Route Visualization',
                        geo=dict(
                            scope='world',
                            showland=True,
                            landcolor='rgb(242, 242, 242)',
                            showocean=True,
                            oceancolor='rgb(204, 204, 255)',
                            showcoastlines=True,
                            coastlinecolor='rgb(204, 204, 204)',
                            showframe=False
                        )
                    ))

    fig.write_html(plotly_filename)
    print(f"Plotly map saved to {plotly_filename}")

def open_in_browser(filename):
    """
    Open the specified file in the default web browser.
    """
    file_path = os.path.abspath(filename)
    webbrowser.open(f'file://{file_path}')

def main():
    parser = argparse.ArgumentParser(description='Generate and visualize optimal route.')
    parser.add_argument('--nodes_file', type=str, required=True, help='Path to the nodes JSON file.')
    parser.add_argument('--start_node', type=str, required=True, help='Start node name.')
    parser.add_argument('--end_node', type=str, required=True, help='End node name.')
    args = parser.parse_args()

    # Load nodes
    nodes = load_nodes(args.nodes_file)
    if not nodes:
        print("Failed to load nodes.")
        return

    # Fetch weather and ocean data
    start_coords = nodes[args.start_node]
    end_coords = nodes[args.end_node]

    weather_data = fetch_weather_data(start_coords[0], start_coords[1], end_coords[0], end_coords[1])
    ocean_data = fetch_ocean_data(start_coords[0], start_coords[1], end_coords[0], end_coords[1])

    if not weather_data or not ocean_data:
        print("Failed to fetch NOAA data.")
        return

    # Find optimal route
    route = find_optimal_route(nodes, args.start_node, args.end_node, weather_data, ocean_data)
    if not route:
        print("Failed to find route.")
        return

    # Visualize route with Folium
    map_filename = 'route_map.html'
    visualize_route_on_map(route, nodes, map_filename)

    # Visualize route with Plotly
    plotly_filename = 'route_plotly.html'
    visualize_route_on_plotly(route, nodes, plotly_filename)

    # Open maps in browser
    open_in_browser(map_filename)
    open_in_browser(plotly_filename)

if __name__ == '__main__':
    main()
