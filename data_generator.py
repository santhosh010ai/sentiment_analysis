import random
import pandas as pd

positive_templates = [
    "I absolutely loved the product!",
    "Fast delivery and excellent service.",
    "Very satisfied with the quality.",
    "This exceeded my expectations.",
    "Great value for money."
]

negative_templates = [
    "Completely disappointed with the purchase.",
    "It stopped working after one use.",
    "Terrible customer service.",
    "Not worth the price.",
    "The worst experience ever."
]

neutral_templates = [
    "It is okay, nothing special.",
    "The product is average.",
    "It meets the basic requirements.",
    "Neither good nor bad.",
    "Service was fine."
]

def generate_feedback():
    data = []
    for sentiment, templates in [("positive", positive_templates), ("negative", negative_templates), ("neutral", neutral_templates)]:
        for _ in range(333):
            feedback = " ".join(random.choices(templates, k=random.randint(1, 3)))
            data.append({"text": feedback, "sentiment": sentiment})
    df = pd.DataFrame(data)
    df.to_csv("sentiment_data.csv", index=False)
    print("Data saved to sentiment_data.csv")

if __name__ == "__main__":
    generate_feedback()
