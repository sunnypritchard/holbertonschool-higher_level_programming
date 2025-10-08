#!/usr/bin/env python3
"""Fetch posts from a RESTful API and save them to a CSV file."""
import csv
import requests


def fetch_and_print_posts():
    """Fetch posts and print the HTTP status code and titles.

    Kept for backward compatibility with prior behavior.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve posts. Status Code:", response.status_code)
        return

    print("Status Code:", response.status_code)     # Print the status code
    for post in response.json():
        print(f"{post['title']}")


def fetch_and_save_posts(csv_path="posts.csv"):
    """Fetch posts and write them to CSV as a list of dictionaries.

    Each post dictionary contains keys: id, title, body.

    Args:
        csv_path (str): Path to output CSV file. Defaults to 'posts.csv'.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to retrieve posts. Status Code:", response.status_code)
        return

    posts = []
    for post in response.json():
        posts.append({
            "id": post.get("id"),
            "title": post.get("title", ""),
            "body": post.get("body", ""),
        })

    # Write to CSV using csv.DictWriter
    fieldnames = ["id", "title", "body"]
    try:
        with open(csv_path, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                writer.writerow(post)
        print(f"Wrote {len(posts)} posts to {csv_path}")
    except OSError as e:
        print(f"Failed to write CSV file {csv_path}: {e}")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
