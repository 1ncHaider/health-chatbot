from transformers import pipeline

# Load a pre-trained model for intent/symptom detection
# For demo purposes, using sentiment-analysis (replace with health-specific model for production)
classifier = pipeline("sentiment-analysis")

def analyze_message(message):
    # Placeholder for more advanced NLU
    result = classifier(message)
    return result[0]
