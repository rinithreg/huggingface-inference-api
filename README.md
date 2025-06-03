# HuggingFace Inference Container

This project provides a scalable FastAPI container for running inference using any HuggingFace model. Demonstrated using `distilbert-base-uncased-finetuned-sst-2-english`.

## Features
- Docker-ready REST API
- Parallel request handling
- HuggingFace model inference
- Test notebook client

## How to Run
```bash
docker build -t hf-infer .
docker run -p 8000:8000 hf-infer
