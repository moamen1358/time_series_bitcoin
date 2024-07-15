from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('model_1.h5')

# Define FastAPI app
app = FastAPI()

# Define input data model using Pydantic
class InputData(BaseModel):
    data: list[float]

# Endpoint to handle prediction
@app.post("/predict")
def predict(input_data: InputData):
    try:
        # Convert input_data to numpy array
        input_array = np.array([input_data.data])

        # Perform prediction
        prediction = model.predict(input_array)

        # Assuming your model predicts a single value
        predicted_value = prediction[0][0]

        # Return the predicted value in a JSON-compatible format
        return {"predicted_value": float(predicted_value)}  

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

