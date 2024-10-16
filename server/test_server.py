import pytest
from flask import Flask
from server import app

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client

def test_home(client):
	response = client.get('/')
	assert response.status_code == 200
	assert response.data.decode('utf-8') == "Let's build a flight delay prediction api!"

def test_predict_valid_input(client, mocker):
	mock_model = mocker.patch('server.model')
	mock_model.predict_proba.return_value = [[0.7, 0.3]]

	response = client.get('/predict?day_of_week=3&airport_id=123')
	assert response.status_code == 200
	data = response.get_json()
	assert data['prediction'] == [0.7, 0.3]
	assert data['confidence_percent'] == 70
	assert data['delayed_percent'] == 30
	assert data['message'] == "The flight is unlikely to be delayed."

def test_predict_invalid_input(client):
	response = client.get('/predict?day_of_week=abc&airport_id=123')
	assert response.status_code == 400
	data = response.get_json()
	assert data['error'] == 'Invalid input. Please provide integers for day_of_week and airport_id.'