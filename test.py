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
    try:
        data = response.json()
        if 'prediction' in data:
            print(f"Text: {sentence}\nPrediction: {data['prediction']}\n")
        else:
            print(f"Text: {sentence}\nUnexpected Response: {data}\n")
    except Exception as e:
        print(f"Text: {sentence}\nError parsing response: {e}\nStatus Code: {response.status_code}\nResponse Text: {response.text}\n")
