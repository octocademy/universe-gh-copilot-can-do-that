# Flight Delay Prediction API ✈️

## Description

This project implements a flight delay prediction API using Flask. It predicts the likelihood of a flight being delayed based on the day of the week and the airport ID. The API leverages a pre-trained machine learning model to provide predictions.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/flight-delay-prediction-api.git
    ```
2. Navigate to the project directory:
    ```sh
    cd flight-delay-prediction-api
    ```
3. Create a virtual environment:
    ```sh
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
5. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the pre-trained model file `model.pkl` in the project directory.
2. Run the Flask server:
    ```sh
    python server.py
    ```
3. The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### Home
- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns a welcome message.

### Predict
- **URL:** `/predict`
- **Method:** `GET`
- **Query Parameters:**
    - `day_of_week` (int): The day of the week (0-6).
    - `airport_id` (int): The ID of the airport.
- **Response:**
    - `prediction` (list): The probabilities of not being delayed and being delayed.
    - `confidence_percent` (int): The confidence percentage of the flight not being delayed.
    - `delayed_percent` (int): The percentage chance of the flight being delayed.
    - `message` (str): A message indicating the likelihood of delay.

## Example Request

```sh
curl "http://127.0.0.1:5000/predict?day_of_week=3&airport_id=124"
```

## License

This project is licensed under the MIT License.