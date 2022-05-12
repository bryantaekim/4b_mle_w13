from transformers import pipeline
from pydantic import BaseModel
calss PredictionRequest(BaseModel):
	query_string: str

@app.post("my_endpoint"):
def my_endpooint(request: PredictionRequest):
	sentiment_model = pipeline("Sentiment-Analysis")

	request = PredictionRequest(sentiment_query_sentence = "I love you")
	sentiment = sentiment_model(sentiment_query_sentence)
	print(f"Sentiment test:" {sentiment_query_sentence} == {sentiment})
	