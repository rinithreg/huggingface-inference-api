# HuggingFace Inference API with FastAPI & Docker

This project demonstrates how to serve any pre-trained HuggingFace model using a FastAPI container that supports parallel inference requests. It includes a client notebook to test concurrent POST requests.

## 📁 Folder Structure

- `app/`: FastAPI application and HuggingFace model logic
- `client/`: Notebook to send parallel requests
- `Dockerfile`: For containerizing the server
- `requirements.txt`: Python dependencies

## 🚀 Run the Server

```bash
# Option 1: With Python locally
pip install -r requirements.txt
uvicorn app.main:app --reload

# Option 2: With Docker
docker build -t hf-inference-api .
docker run -p 8000:8000 hf-inference-api

## 🧪 Send Parallel Requests
Open client/send_requests.ipynb and run all cells. It will POST requests to the API endpoint and show response times.

## 🧠 Model Used
This project uses distilbert-base-uncased-finetuned-sst-2-english, a lightweight sentiment analysis model. It was chosen for demo because:
- It’s small and fast
- Covers a well-understood NLP task (sentiment classification)
- Works out-of-the-box with Hugging Face's pipeline

## 📦 Requirements
Python 3.8+
FastAPI
Uvicorn
Transformers
Requests

## 📄 License
MIT
