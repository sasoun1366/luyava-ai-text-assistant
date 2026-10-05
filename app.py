from flask import Flask, request, jsonify
import os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY", "dev-secret")

@app.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    if data.get("api_key") != API_KEY:
        return jsonify({"error": "unauthorized"}), 401

    message = data.get("message", "")
    return jsonify({"reply": "You said: " + message})

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
