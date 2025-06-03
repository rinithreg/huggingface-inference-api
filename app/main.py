from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
from app.model import predict # Importing the prediction function

# Initialize FastAPI app
app = FastAPI()


# Define request schema using Pydantic
class InferenceRequest(BaseModel):
    inputs: List[str]  # List of text inputs for sentiment analysis


# Define the POST endpoint for inference
@app.post("/infer")
def inference(req: InferenceRequest):
    try:
        # Perform prediction using the model
        result = predict(req.inputs)
        return {"success": True, "results": result}
    except Exception as e:
        # Catch and return any error
        return {"success": False, "error": str(e)}
