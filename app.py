# app.py
from dotenv import load_dotenv
import os
import requests
from flask import Flask, request, render_template, jsonify

# Load environment variables from .env
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
BASE_URL = "https://api.groq.com/openai/v1"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form.get("question")
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama-3.1-8b-instant",
            "messages": [{"role": "user", "content": question}],
            "temperature": 0.7
        }

        response = requests.post(f"{BASE_URL}/chat/completions", json=data, headers=headers)
        if response.status_code == 200:
            answer = response.json()["choices"][0]["message"]["content"]
        else:
            answer = f"API Error: {response.text}"

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
