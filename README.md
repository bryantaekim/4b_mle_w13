# 4b_mle_w13 - How to Use this containerized web application

## Hello World
1. Open your local browser
2. Type "localhost:8000/health"
3. You will see a returned string value, "Service is online."

## Hugging Face Sentiment analysis
1. Open your local browser
2. Type "localhost:8000/docs"
3. You will see a FastAPI webpage
![image](https://user-images.githubusercontent.com/34020408/168189387-5a4e2321-bcee-45fc-b378-bef8c64b5c0d.png)

4. Click on "Try it out"
5. Enter your own query in the Requested Body,

{
  "query_string": "I love you"
}

6.Hit "Execute"
7.You will have a sentiment result as below,

{
  "Sentiment": [
    {
      "label": "POSITIVE",
      "score": 0.9998656511306763
    }
  ]
}
