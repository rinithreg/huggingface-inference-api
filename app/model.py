from transformers import pipeline

# Load pre-trained HuggingFace sentiment analysis model
nlp_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


# Define predict function to be called by the FastAPI app
def predict(text: str):
    return nlp_pipeline(text)