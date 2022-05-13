from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictionRequest(BaseModel):
	query_string: str

@app.get('/health')
def health():
	return 'Service is online.'

@app.post("/my-endpoint")
def my_endpooint(request: PredictionRequest):
	sentiment_model = pipeline("sentiment-analysis")

	sentiment = sentiment_model(request.query_string)
	print(f"Sentiment test: {request.query_string} == {sentiment}")
	return {"Sentiment" : sentiment}
	
