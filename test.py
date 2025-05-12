import requests

test_sentences = [
    "I absolutely loved the experience. Everything was perfect!",

    "Amazing service and great attention to detail.",

    "The product quality is outstanding. Will recommend to others.",

    "Super fast delivery and well packaged.",
    "It made my day better. Very happy with this purchase."
]

for sentence in test_sentences:
    response = requests.post('http://127.0.0.1:5000/predict', json={"text": sentence})
    print(f"Text: {sentence}\nPrediction: {response.json()['prediction']}\n")

