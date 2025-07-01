# ignore: no-name-in-module
import pytest

from fastapi.testclient import TestClient
from shifttask.main import app

client = TestClient(app)


def test_login_and_get_salary():

    response = client.post(
        "/token",
        data={"grant_type": 'password', "username": "john_doe", "password": "secret123"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data
    access_token = token_data["access_token"]


    response = client.get(
        "/salary",
        headers={"Authorization": f"Bearer {access_token}"}
    )
    assert response.status_code == 200
    salary_info = response.json()
    assert "salary" in salary_info
    assert "next_raise_date" in salary_info


def test_salary_without_token():

    response = client.get("/salary")
    assert response.status_code == 401  # Unauthorized


def test_login_with_wrong_password():
    response = client.post(
        "/token",
        data={"username": "john_doe", "password": "wrongpassword"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 400 or response.status_code == 401


def test_login_with_invalid_user():
    response = client.post(
        "/token",
        data={"username": "nonexistent_user", "password": "password"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 400 or response.status_code == 401
