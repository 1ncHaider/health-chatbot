from flask import Flask, request, jsonify
from nlp import analyze_message
from handlers import handle_chat, handle_appointment, handle_doctor_connection, handle_faq, handle_health_tip

app = Flask(__name__)

@app.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    nlp_result = analyze_message(user_message)
    response = handle_chat(user_message, nlp_result)
    return jsonify(response)

@app.route("/api/appointment", methods=["POST"])
def appointment():
    user_info = request.json
    response = handle_appointment(user_info)
    return jsonify(response)

@app.route("/api/doctor", methods=["POST"])
def doctor():
    user_info = request.json
    response = handle_doctor_connection(user_info)
    return jsonify(response)

@app.route("/api/faq", methods=["GET"])
def faq():
    question = request.args.get("q", "")
    response = handle_faq(question)
    return jsonify(response)

@app.route("/api/health_tip", methods=["GET"])
def health_tip():
    response = handle_health_tip()
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
