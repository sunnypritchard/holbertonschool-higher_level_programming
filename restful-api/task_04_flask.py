#!/usr/bin/env python3
"""A simple Flask API with multiple endpoints."""

from flask import Flask, jsonify, request


app = Flask(__name__)

# In-memory user storage (empty submission for task requirements)
users = {}


@app.route("/")
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """Return a JSON list of all usernames."""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    """Return a simple status check."""
    return "OK", 200


@app.route("/users/<username>")
def get_user(username):
    """Return user data if found, otherwise an error message."""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from JSON payload."""
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": f"User '{username}' added successfully!",
        "user": users[username]
    }), 201
