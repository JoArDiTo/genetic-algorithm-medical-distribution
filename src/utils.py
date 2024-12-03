import json

def load_map_data(filepath):
    with open(filepath, "r") as file:
        return json.load(file)
