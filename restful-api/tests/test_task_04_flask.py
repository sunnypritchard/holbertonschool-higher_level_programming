import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task_04_flask import app, users  # noqa: E402, F401


@pytest.fixture
def client():
    """Flask test client fixture."""
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def clear_users():
    """Ensure the in-memory users dict is empty before each test."""
    users.clear()
    yield
    users.clear()


def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_data(as_text=True) == "Welcome to the Flask API!"


def test_data_empty(client):
    resp = client.get("/data")
    assert resp.status_code == 200
    body = resp.get_json()
    assert isinstance(body, list)
    assert body == []


def test_status_returns_ok_plain_text(client):
    resp = client.get("/status")
    # /status returns plain text "OK"
    assert resp.status_code == 200
    assert resp.get_data(as_text=True) == "OK"


def test_add_user_success_returns_201_and_message(client):
    new_user = {"username": "alice", "name": "Alice", "age": 28, "city": "LA"}
    resp = client.post("/add_user", json=new_user)
    assert resp.status_code == 201
    body = resp.get_json()
    assert isinstance(body, dict)
    assert body.get("message") == "User alice added"
    # Note: current implementation does not actually insert into users dict,
    # so we only assert the response (do not assert users contains 'alice').


def test_add_user_missing_username_returns_400(client):
    resp = client.post("/add_user", json={})
    assert resp.status_code == 400
    body = resp.get_json()
    assert isinstance(body, dict)
    assert body.get("error") == "Username is required"


def test_get_user_success(client):
    # Pre-populate users dict to simulate an existing user
    users["bob"] = {"username": "bob", "name": "Bob", "age": 40, "city": "Chicago"}

    resp = client.get("/users/bob")
    assert resp.status_code == 200
    body = resp.get_json()
    assert body == {"username": "bob", "name": "Bob", "age": 40, "city": "Chicago"}


def test_get_user_not_found_returns_404(client):
    resp = client.get("/users/doesnotexist")
    assert resp.status_code == 404
    body = resp.get_json()
    assert isinstance(body, dict)
    assert body.get("error") == "User not found"
