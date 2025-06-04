# Health Chatbot

A multi-platform, AI-powered health chatbot built with Python (Flask + Transformers).  
Features include symptom checking, appointment booking, health tips, FAQs, and doctor connection.

## Features

- AI/ML-powered symptom checker (Hugging Face Transformers, customizable)
- Appointment booking (demo logic)
- FAQ and health tips
- Connect to real doctors (demo data)
- Web API (Flask) for easy integration
- Extendable to messaging apps (Telegram, WhatsApp, etc.)

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the API server:
   ```
   python app.py
   ```

3. Send POST requests to `/api/chat` with a JSON body:
   ```json
   { "message": "I have a headache" }
   ```

## Extending

- Integrate with messaging apps (see `handlers.py`)
- Replace the ML model in `nlp.py` with a health-specific intent/symptom detection model
- Add persistent storage, authentication, or real doctor APIs as needed
