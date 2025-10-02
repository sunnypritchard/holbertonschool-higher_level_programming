#!/usr/bin/python3
"""Module that convert a CSV file to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV file to JSON format and save to data.json.

    Args:
        csv_filename (str): The name/path of the CSV file to convert

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:

        data = []
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return False

    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return False


if __name__ == "__main__":
    csv_file = "data.csv"
    convert_csv_to_json(csv_file)
    print(f"Data from {csv_file} has been converted to data.json")
