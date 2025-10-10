#!/usr/bin/python3
"""
This module defines a simple API using Flask,
with multiple methods to access different routes
and handle a POST request.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """
    This method defines a route for the root URL.

    Returns:
        A welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def jsonify_data():
    """
    This method allows access to the 'data' route containing users data.

    Returns:
        A JSON containing the list of all users.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    This method returns the status OK.
    """
    return "OK"


@app.route("/users/<string:username>")
def dynamic_route(username):
    """
    This method allows dynamic routing when trying
    to access a specific user’s data.

    Arg:
        username: The name of the user for the route access.
    Returns:
        The JSON user data if the user exists.
        Else returns 'error': 'User not found'.
    """
    if username in users:
        response = jsonify(users[username])
        return response, 200
    else:
        response = jsonify({"error": "User not found"})
        return response, 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    This method allows a POST request to add a new user
    using JSON data.

    Expected JSON format:
        {
            "username": "name",
            "data": {"key": "value"}
        }

    Returns:
        If a username is provided and valid, returns a confirmation message
        with the user data and status code 201.
        Else returns 'error': 'Username is required' with status code 400.
    """
    user_data = request.get_json()

    if not user_data or "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data["username"]
    users[username] = user_data.get("data", {})

    return jsonify({
        "message": "User added",
        "user": {username: users[username]}
    }), 201


if __name__ == "__main__":
    app.run()
