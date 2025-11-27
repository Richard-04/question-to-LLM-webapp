# app.py
import os

# Only use load_dotenv when running locally
if os.getenv("RENDER") is None:  # Render automatically sets some env variables
    from dotenv import load_dotenv
    load_dotenv()  # Loads variables from your local .env file

# Get the API key
API_KEY = os.getenv("GROQ_API_KEY")

# Example usage
if API_KEY is None:
    raise ValueError("GROQ_API_KEY is not set! Check your environment variables.")

print("API Key loaded successfully!")

# Your app logic here
# For example, if using FastAPI or Flask, start the server
# from flask import Flask
# app = Flask(__name__)
# ...
