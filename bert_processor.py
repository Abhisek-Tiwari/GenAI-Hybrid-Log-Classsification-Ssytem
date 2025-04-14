from sentence_transformers import SentenceTransformer
import joblib

transformer = SentenceTransformer('all-MiniLM-L6-v2')
classifier = joblib.load('models/log_classifier.joblib')

def classify_with_bert(log_message):
    embedding = transformer.encode(log_message)
    probabilities = classifier.predict_proba([embedding])[0]
    if max(probabilities) < 0.5:
        return "Unclassified"
    predicted_class = classifier.predict([embedding])[0]

    return predicted_class