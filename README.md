# Bitcoin Time Series Prediction

## Overview

This project aims to predict the price of Bitcoin using time series forecasting techniques. It utilizes machine learning models trained on historical Bitcoin price data to make predictions about future prices.

## Model loss

{'mae': 561.7786,

'mse': 1151999.0,

'rmse': 1073.3121,

'mape': 2.5123477,

'mase': 0.9868893479373553}

## Features

- **Model:** Utilizes TensorFlow for model training and prediction.
- **API:** Built with FastAPI to provide a RESTful API endpoint for making predictions.
- **Deployment:** Deployed using Uvicorn for serving the FastAPI application.

## Requirements

Ensure you have the following installed:

- Python 3.10.12
- Libraries listed in `requirements.txt`

# installation guide

1. create new conda environment

```bash
conda create -n bitcoin python=3.10.12
```

2. activate the enviroment

```bash
conda activate bitcoin
```

3. install the packages needed for the project

```bash
pip install -r requirements.txt
```

4. Start FastAPI Application

```bash
uvicorn main:app --reload
```

## Usage

### Using Postman

1. Open Postman.
2. Create a new request.
3. Set the request method to POST.
4. Enter the URL of your FastAPI application along with the specific endpoint that expects the image.
   - Example URL: `http://127.0.0.1:8000/predict`
5. Click on the "Body" tab.
6. click on ''raw''.
7. then click on dropdown menu and choose ''json''.
8. Click the "Send" button to send the request to your FastAPI application.

## Example Input

- {
  "data": [
  123.65499,
  125.455,
  108.58483,
  ...,
  121.33866,
  120.65533,
  121.795
  ]
  }

## Contributors

- Mu'min
