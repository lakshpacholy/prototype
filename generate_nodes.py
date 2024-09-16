import numpy as np
import json
import argparse
import sys
import concurrent.futures

def generate_grid_coordinates(start_lat, start_lon, end_lat, end_lon, spacing):
    try:
        lats = np.linspace(start_lat, end_lat, int(abs(end_lat - start_lat) / spacing) + 1)
        lons = np.linspace(start_lon, end_lon, int(abs(end_lon - start_lon) / spacing) + 1)
        grid_points = [(lat, lon) for lat in lats for lon in lons]
        return grid_points
    except Exception as e:
        print(f"Error generating grid coordinates: {e}", file=sys.stderr)
        sys.exit(1)

def is_valid_point(lat, lon):
    depth = get_depth_from_bathymetric_data(lat, lon)
    # Placeholder for actual validation logic, currently allowing all depths
    # For example, we could exclude points with depths less than a threshold.
    return depth > 5  # Exclude points with depth < 5 meters as an example

def get_depth_from_bathymetric_data(lat, lon):
    # Simulated bathymetric data retrieval
    return np.random.uniform(10, 50)  # Example depth range between 10m to 50m

def process_point(point):
    lat, lon = point
    return is_valid_point(lat, lon)

def generate_valid_nodes(start_lat, start_lon, end_lat, end_lon, spacing, parallel=False):
    grid_points = generate_grid_coordinates(start_lat, start_lon, end_lat, end_lon, spacing)
    valid_nodes = {}
    count = 0

    if parallel:
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = list(executor.map(process_point, grid_points))
    else:
        results = [is_valid_point(lat, lon) for lat, lon in grid_points]

    for i, (lat, lon) in enumerate(grid_points):
        if results[i]:
            node_name = f'Node{count + 1}'
            valid_nodes[node_name] = (lat, lon)
            count += 1

    return valid_nodes

def save_nodes_to_file(nodes, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(nodes, file)
        print(f"Nodes successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving nodes to file: {e}", file=sys.stderr)
        sys.exit(1)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate navigable nodes for ocean route.')
    parser.add_argument('--start_lat', type=float, required=True, help='Latitude of the start location')
    parser.add_argument('--start_lon', type=float, required=True, help='Longitude of the start location')
    parser.add_argument('--end_lat', type=float, required=True, help='Latitude of the end location')
    parser.add_argument('--end_lon', type=float, required=True, help='Longitude of the end location')
    parser.add_argument('--spacing', type=float, default=0.1, help='Spacing between grid points in degrees')
    parser.add_argument('--parallel', action='store_true', help='Use parallel processing')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()

    if args.spacing <= 0:
        print("Error: Spacing must be a positive value.", file=sys.stderr)
        sys.exit(1)

    valid_nodes = generate_valid_nodes(args.start_lat, args.start_lon, args.end_lat, args.end_lon, args.spacing, args.parallel)
    
    if not valid_nodes:
        print("No valid nodes were generated. Please check the input parameters.", file=sys.stderr)
        sys.exit(1)

    save_nodes_to_file(valid_nodes, 'valid_nodes.json')
    print(f"{len(valid_nodes)} valid nodes have been generated and saved to 'valid_nodes.json'")
