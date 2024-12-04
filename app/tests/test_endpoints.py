import pytest
import sys
import os
import json

# Add the root directory of your project to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app

data = [
    {
        "description": "Sedan with sunroof",
        "fuel_type": "Gasoline",
        "horse_power": 180,
        "manufacturer": "Tesla",
        "model_name": "Honda Civic",
        "model_year": 2022,
        "purchase_price": 25000.5,
        "vin": 123456
    }
]

mock_data = {
    "description": "Sedan with sunroof",
    "fuel_type": "Gasoline",
    "horse_power": 180,
    "manufacturer": "Tesla",
    "model_name": "Honda Civic",
    "model_year": 2022,
    "purchase_price": 25000.5,
    "vin": 123456
}


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


@pytest.mark.get
def test_get_vehicles(client):
    """
    Gets the data and checks the status code

    Args:
        client: tool that allows you to run HTTP requests to Flask application without running live server
    """
    response = client.get('/vehicle')
    assert response.status_code == 200
    assert json.loads(response.data) == data


@pytest.mark.get
def test_get_vehicle_with_bad_vin(client):
    """
    Gets the vehicle with vin 1 and checks the status code, should send 400 since vehicle with vin 1 does not exist

    Args:
        client: tool that allows you to run HTTP requests to Flask application without running live server
    """
    response = client.get('/vehicle/1')
    assert response.status_code == 400
    assert json.loads(response.data) != mock_data

@pytest.mark.get
def test_get_vehicle_with_correct_vin(client):
    """
    Gets the vehicle with vin 1 and checks the status code, should send 200 to indicate success

    Args:
        client: tool that allows you to run HTTP requests to Flask application without running live server
    """
    response = client.get('/vehicle/123456')
    assert response.status_code == 200
    assert json.loads(response.data) == mock_data

@pytest.mark.put
def test_post_vehicle_with_bad_vin(client):
    """
    Gets the vehicle with vin 1 and checks the status code, should send 400 since vehicle with vin 1 does not exist

    Args:
        client: tool that allows you to run HTTP requests to Flask application without running live server
    """
    response = client.put('/vehicle/1')
    assert response.status_code == 400
    assert json.loads(response.data) != mock_data

@pytest.mark.post
def test_bad_post_vehicle(client):
    """
    Gets the vehicle with vin 1 and checks the status code, should send 405 Method Not Allowed
    since post request does not have json

    Args:
        client: tool that allows you to run HTTP requests to Flask application without running live server
    """
    response = client.post('/vehicle/123456')
    assert response.status_code == 405

@pytest.mark.delete
def test_error_delete_vehicle(client):
    """
    Deletes a vehicle with vin of 1, should send 400 status code to indicate error

    Args:
        client: tool that allows you to run HTTP requests to Flask application without running live server

    """
    response = client.delete('/vehicle/1')
    assert response.status_code == 400

@pytest.mark.delete
def test_delete_vehicle(client):
    """
    Deletes a vehicle with vin of 1, should send 204 to indicate no content and succesful deletion

    Args:
        client: tool that allows you to run HTTP requests to Flask application without running live server

    """
    response = client.delete('/vehicle/123456')
    assert response.status_code == 204
