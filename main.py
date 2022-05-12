from transformers import pipeline
from pydantic import BaseModel
calss predictionRequest(BaseModel):
	query_string: str

@app.post("my_endpoint"):
def my_endpooint(request: predictionRequest):
	sentiment_model = pipeline("Sentiment-Analysis")

	request = predictionRequest(sentiment_query_sentence = "I love you")
	sentiment = sentiment_model(sentiment_query_sentence)
	print(f"Sentiment test:" {sentiment_query_sentence} == {sentiment})
	