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
