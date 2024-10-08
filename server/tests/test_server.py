import sys
import os
import pytest
from flask import Flask
from flask.testing import FlaskClient

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server import app

@pytest.fixture
def client() -> FlaskClient:
    with app.test_client() as client:
        yield client

def test_home(client: FlaskClient):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Let's build a flight delay prediction api!" in response.data

def test_predict_missing_parameters(client: FlaskClient):
    response = client.get('/predict')
    assert response.status_code == 400
    assert response.json == {"error": "Missing parameters"}

def test_predict_invalid_parameters(client: FlaskClient):
    response = client.get('/predict?day_of_week=abc&airport_id=xyz')
    assert response.status_code == 400
    assert response.json == {"error": "Invalid parameter types"}

def test_predict_valid_parameters(client: FlaskClient, mocker):
    # Mock the model's predict_proba method
    mock_model = mocker.patch('server.model.Model.predict_proba', return_value=[[0.7, 0.3]])
    
    response = client.get('/predict?day_of_week=1&airport_id=123')
    assert response.status_code == 200
    assert response.json == {
        "model_prediction": "Not Delayed",
        "confidence_percent": 70,
        "delayed_percent": 30,
        "sentence": "The flight will not be delayed."
    }
    mock_model.assert_called_once_with([[1, 123]])

def test_predict_delayed(client: FlaskClient, mocker):
    # Mock the model's predict_proba method
    mock_model = mocker.patch('server.model.predict_proba', return_value=[[0.4, 0.6]])
    
    response = client.get('/predict?day_of_week=1&airport_id=123')
    assert response.status_code == 200
    assert response.json == {
        "model_prediction": "Delayed",
        "confidence_percent": 40,
        "delayed_percent": 60,
        "sentence": "The flight will be delayed."
    }
    mock_model.assert_called_once_with([[1, 123]])