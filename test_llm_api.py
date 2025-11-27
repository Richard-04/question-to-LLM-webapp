import requests

API_KEY = os.getenv("GROQ_API_KEY")
URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "llama-3.1-8b-instant",
    "messages": [{"role": "user", "content": "Hello, are you working?"}]
}

response = requests.post(URL, headers=headers, json=data)
print(response.json())