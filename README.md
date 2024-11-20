# Flight Delay Prediction API ✈️

## Description

This project implements a flight delay prediction API using Flask. It predicts the likelihood of a flight being delayed based on the day of the week and the airport ID. The API leverages a pre-trained machine learning model to provide predictions.

### Watch the video here 🚀
https://www.youtube.com/embed/OupqM6FFbn4


## Features

- **Prediction Endpoint**: Predicts flight delays based on input parameters.
- **CORS Enabled**: Allows cross-origin requests for flexibility in frontend integrations.
- **Extensible**: Easily deployable to platforms like Azure Functions for scalable serverless deployments.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- `model.pkl` file containing the trained machine learning model

## Installation

1. **Clone the Repository**
    ```sh
    git clone https://github.com/your-username/flight-delay-prediction-api.git
    cd flight-delay-prediction-api
    ```

2. **Create a Virtual Environment**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Place the Model File**
    Ensure the `model.pkl` file is located in the root directory of the project.

## Usage

1. **Run the Server**
    ```sh
    python server.py
    ```

2. **Access the API**
    - Home Endpoint:
        ```
        GET http://localhost:5000/
        ```
      **Response:**
        ```
        Let's build a flight delay prediction api!
        ```

    - Prediction Endpoint:
        ```
        GET http://localhost:5000/predict?day_of_week=<DAY_OF_WEEK>&airport_id=<AIRPORT_ID>
        ```
      **Parameters:**
        - `day_of_week`: Integer (0=Monday, 6=Sunday)
        - `airport_id`: Integer representing the airport identifier

      **Response:**
        ```json
        {
            "model_prediction": "Not Delayed",
            "confidence_percent": 60,
            "delayed_percent": 40,
            "sentence": "The flight will not be delayed."
        }
        ```

## Example

```sh
curl "http://localhost:5000/predict?day_of_week=2&airport_id=15"
```

## Deployment
To deploy this API as an Azure Function:

Follow the Azure Functions Setup Guide to set up your environment.
Convert the Flask routes to Azure Function HTTP triggers.
Deploy using the Azure CLI:

```sh
az functionapp create --resource-group YourResourceGroup --consumption-plan-location YourLocation --runtime python --runtime-version 3.8 --functions-version 3 --name YourFunctionAppName --storage-account YourStorageAccount
func azure functionapp publish YourFunctionAppName
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

Distributed under the MIT License.

## Resources to learn more

- [Using GitHub Copilot in your IDE: Tips, tricks, and best practices](https://github.blog/2024-03-25-how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/)
- [10 unexpected ways to use GitHub Copilot](https://github.blog/2024-01-22-10-unexpected-ways-to-use-github-copilot/)
- [How to use Github Copilot in the CLI](https://www.youtube.com/watch?v=fHwtrOcLAnI&t=32s)
- [Prompt crafting with GitHub Copilot](https://www.youtube.com/watch?v=GPLUGJsVx0s)
- [GitHub Copilot Metrics API GA](https://github.blog/changelog/2024-10-30-github-copilot-metrics-api-ga-release-now-available/)
- [GitHub_Copilot_CheatSheet_Guide](https://github.com/user-attachments/files/17836574/8.5x11_Final_GitHub_Copilot_CheatSheet_Guide_Back_Purple_CMYK.pdf)

