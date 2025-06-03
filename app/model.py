from transformers import pipeline

# Load pre-trained sentiment analysis pipeline
nlp_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def predict(text: str):
    return nlp_pipeline(text)
