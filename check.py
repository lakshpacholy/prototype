import json

def load_nodes(filename):
    try:
        with open(filename, 'r') as file:
            nodes = json.load(file)
        print("Loaded nodes successfully.")
        return nodes
    except Exception as e:
        print(f"Error loading nodes: {e}")
        return None

# Test loading the valid_nodes.json
nodes = load_nodes('valid_nodes.json')
if nodes:
    print(nodes)
