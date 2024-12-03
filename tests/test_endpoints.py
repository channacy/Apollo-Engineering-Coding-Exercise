import pytest
from app import app

@pytest.mark.get_request
def test_get_vehicles():
    response = app.test_client().get('/vehicle')
    assert response.status_code == 200