
## Overview
This project is a lightweight AI-driven text classification system for customer sentiment analysis. It classifies feedback into Positive, Negative, or Neutral.

## Features
- Custom synthetic data generator
- Text preprocessing (cleaning, TF-IDF)
- Logistic Regression model (no deep learning)
- REST API built with Flask
- Evaluation: accuracy, precision, recall, F1-score

## How to Run

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


3. **Train model**:
   ```bash
   python model.py
   ```

4. **Start API server**:
   ```bash
   python api.py
   ```

5. **Send a request**:
   ```bash
   curl -X POST http://127.0.0.1:5000/predict \
   -H "Content-Type: application/json" \
   -d '{"text": "The product is amazing and arrived early!"}'
   ```

## Justification
- **TF-IDF + Logistic Regression** provides interpretable and efficient classification.
- **Hand-crafted synthetic data** ensures varied and labeled inputs.
- **Flask API** is lightweight and easy to integrate into other systems.

## Assumptions & Limitations
- No pre-trained models or embeddings used.
- Works best with short, single-topic feedback.

## Bonus Ideas
- In-memory cache can be added using `functools.lru_cache` or a dictionary.
- Faster training using `HashingVectorizer` or reduced max_features in TF-IDF.
- For deployment: Use Docker + Gunicorn on AWS EC2 or Lambda with API Gateway.
