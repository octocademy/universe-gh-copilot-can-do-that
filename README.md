# Flight Delay Prediction ✈️

This repository contains a flight delay prediction application. The application uses a logistic regression model to predict the likelihood of a flight being delayed based on the day of the week and the arrival airport.

## Repository Structure 📚

- [`client/`](https://github.com/LadyKerr/msft-build-copilot-demo/tree/927cb5d8a02a584d81dba89f6bf7eda1667039a3/client): Contains the frontend code for the application, built with React and Material-UI.
- [`server/`](https://github.com/LadyKerr/msft-build-copilot-demo/tree/927cb5d8a02a584d81dba89f6bf7eda1667039a3/server): Contains the backend code for the application, which serves the prediction API.
- [`data/flights.csv`](https://github.com/LadyKerr/msft-build-copilot-demo/blob/927cb5d8a02a584d81dba89f6bf7eda1667039a3/data/flights.csv): The dataset used for training the model.
- [`manage-flight-data.ipynb`](https://github.com/LadyKerr/msft-build-copilot-demo/blob/927cb5d8a02a584d81dba89f6bf7eda1667039a3/manage-flight-data.ipynb): A Jupyter notebook that contains the data analysis and model training process.
- [`server/model.pkl`](https://github.com/LadyKerr/msft-build-copilot-demo/blob/927cb5d8a02a584d81dba89f6bf7eda1667039a3/server/model.pkl): The trained logistic regression model.

## How to Run ⚒️

1. Start the backend server by running the `server/server.py` script.
2. Start the frontend application by running `npm run dev` in the `client/` directory.

## Features 👀

- The application allows users to select a day of the week and an airport, and then predicts whether a flight will be delayed or not.
- The prediction is made by a logistic regression model trained on the `flights.csv` dataset.

## Contributing 📝

Contributions are welcome! Please feel free to submit a pull request.

## License 🪪

This project is licensed under the terms of the MIT license. See the `LICENSE` file for details.
