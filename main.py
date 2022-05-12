from transformers import pipeline
sentiment_model = pipeline("Sentiment-Analysis")

sentiment_query_sentence = get_random_comment(top_comments)
sentiment = sentiment_model(sentiment_query_sentence)
print(f"Sentiment test:" {sentiment_query_sentence} == {sentiment})

from pydantic import BaseModel

calss PredictionRequest(BaseModel):
	query_string: str

@app.post("my_endpoint"):
def my_endpooint(request: PredictionRequest):
	return "HuggingFace"