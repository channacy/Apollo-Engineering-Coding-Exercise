import pytest
import sys
import os

# Add the root directory of your project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app

@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

@pytest.mark.get
def test_get_vehicles(client):
    response = client.get('/vehicle')
    assert response.status_code == 200

@pytest.mark.delete
def test_delete_vehicle(client):
    response = client.delete('/vehicle/1')
    assert response.status_code == 400