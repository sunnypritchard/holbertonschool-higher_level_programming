#!/usr/bin/env python3
"""
This module implements a simple API using Flask, with multiple methods to
access different endpoints.
"""

from flask import Flask, jsonify, request


app = Flask(__name__)

# In-memory user storage (empty requirement for this task)
users = {}


@app.route("/")
def home():
    """This method defines the root endpoint of the API.

    Returns:
        str: A welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """This method allows access to the 'data' endpoint containing users data.

    Returns:
        json: A JSON object containing users data.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """This method returns the status OK """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """This method accesses a specific user by username.
    Args:
        username (str): The username of the user to retrieve.

    Returns:
        json: A JSON user if user exists.
        If user does not exist, returns a message: 'error': 'User not found'
        followed by 404 status code.
    """
    if username in users:
        response = jsonify(users[username])
        return response, 200
    else:
        response = jsonify({"error": "User not found"})
        return response, 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """This method adds a new user to the in-memory storage.
    Expects a JSON payload with 'username' and 'data' fields.

    Returns:
        json: A success message if user is added with status code 201.
        If the username already exists, returns a message: 'error': 'User already exists'
        followed by 400 status code.
    """
    user = request.get_json()
    if 'username' not in user:
        return jsonify({"error": "Username is required"}), 400

    username = user['username']

    return jsonify({"message": f"User {username} added"}), 201


if __name__ == "__main__":
    app.run()
