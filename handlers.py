import random
from data import FAQS, HEALTH_TIPS, DOCTORS

def handle_chat(message, nlp_result):
    # Basic intent handling
    label = nlp_result.get("label", "neutral")
    if "symptom" in message.lower():
        return {"reply": "Please describe your symptoms in detail."}
    elif "appointment" in message.lower():
        return {"reply": "Would you like to book an appointment? Please provide your preferred date and time."}
    elif "doctor" in message.lower():
        doctor = random.choice(DOCTORS)
        return {"reply": f"Connecting you to {doctor['name']} ({doctor['specialty']}). Contact: {doctor['contact']}"}
    elif "tip" in message.lower():
        tip = random.choice(HEALTH_TIPS)
        return {"reply": tip}
    elif "faq" in message.lower() or "question" in message.lower():
        return {"reply": "Please ask your FAQ, and I’ll try to answer!"}
    else:
        return {"reply": f"I'm here to help with your health-related questions! (NLP Label: {label})"}

def handle_appointment(user_info):
    # Demo: just echo back appointment info
    return {"reply": f"Appointment booked for {user_info.get('name', 'Anonymous')} on {user_info.get('datetime', 'unspecified')}."}

def handle_doctor_connection(user_info):
    doctor = random.choice(DOCTORS)
    return {"reply": f"Connecting you to {doctor['name']} ({doctor['specialty']}). Contact: {doctor['contact']}"}

def handle_faq(question):
    answer = FAQS.get(question, "Sorry, I don't have an answer for that question yet.")
    return {"reply": answer}

def handle_health_tip():
    tip = random.choice(HEALTH_TIPS)
    return {"reply": tip}
