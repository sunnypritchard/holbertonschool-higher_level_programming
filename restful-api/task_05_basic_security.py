#!/usr/bin/python3
"""
This modules defines simple API Security
and Authentication techniques.
"""

from flask_jwt_extended import create_access_token, get_jwt
from flask_jwt_extended import jwt_required, JWTManager
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
        },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
        }
}


@auth.verify_password
def verify_password(username, password):
    """
    This method verify the password provided by the user

    Args:
        username: the username used to login
        password: the password of the user
    """
    if username in users and \
            check_password_hash(users.get(username).get("password"), password):
        return username
    else:
        return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected_auth():
    """
    This method grants access if the user has provided
    valid basic authentication credentials

    Returns:
        On valid credentials: 'Basic Auth: Access Granted'.
        else: '401 Unauthorized' status code.
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def user_login():
    """
    This methods defines a way for the user to login
    using a POST request with it's username and password.

    Returns:
        A JWT token if credentials are valid.
    """
    username = request.json.get("username")
    password = request.json.get("password")

    is_logged = verify_password(username, password)
    if is_logged is not None:
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": users[username]["role"]})
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "invalid credentials"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_auth_only():
    """
    This methods returns a message if the user provides a valid JWT token.

    this function return a string
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_login():
    claim = get_jwt()
    user_role = claim.get("role")
    if user_role == 'admin':
        return "Admin Access: Granted"
    else:
        return {"error": "Admin access required"}, 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
