#!/usr/bin/env python3
"""Module for basic serialization and deserialization tasks."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize data from a JSON file."""
    with open(filename, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    sample_data = {
        'name': 'Alice',
        'age': 30,
        'city': 'New York'
    }

    filename = 'data.json'

    # Serialize and save to file
    serialize_and_save_to_file(sample_data, filename)

    # Load and deserialize from file
    loaded_data = load_and_deserialize(filename)

    print("Loaded Data:", loaded_data)
