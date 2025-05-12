from flask import Flask, request, jsonify
import joblib
from functools import lru_cache
import string

app = Flask(__name__)

model = joblib.load("model.joblib")
vectorizer = joblib.load("vectorizer.joblib")
label_encoder = joblib.load("label_encoder.joblib")

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

@lru_cache(maxsize=128)
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "Missing 'text' in request"}), 400

    cleaned = clean_text(data["text"])
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0][pred]
    label = label_encoder.inverse_transform([pred])[0]

    return jsonify({"sentiment": label, "confidence": round(float(prob), 4)})

if __name__ == "__main__":
    app.run(debug=True)