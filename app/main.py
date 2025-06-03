from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
from app.model import predict

app = FastAPI()

class InferenceRequest(BaseModel):
    inputs: List[str]

@app.post("/infer")
def inference(req: InferenceRequest):
    try:
        result = predict(req.inputs)
        return {"success": True, "results": result}
    except Exception as e:
        return {"success": False, "error": str(e)}
