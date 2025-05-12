import pandas as pd
import string
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# Load data
df = pd.read_csv("sentiment_data.csv")

# Preprocessing
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

df["clean_text"] = df["text"].apply(clean_text)

# Encoding labels
le = LabelEncoder()
df["label"] = le.fit_transform(df["sentiment"])

# Feature extraction
vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(df["clean_text"])
y = df["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Save model and vectorizer
joblib.dump(model, "model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")
joblib.dump(le, "label_encoder.joblib")

# Evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=le.classes_))