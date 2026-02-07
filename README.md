🔹 Project Title

AI Text → Explanation → Audio Generator using Gemini & FastAPI

🔹 Project Description

This project is a web-based AI application that converts user-entered text into:

Clear AI-generated explanation using Google Gemini API

Spoken audio output using Text-to-Speech (gTTS)

It demonstrates the integration of:

Generative AI

Web backend (FastAPI)

Audio processing

Secure API key handling with .env

🔹 Features

Accepts user text input from browser

Generates simple English explanation using Gemini AI

Converts explanation into MP3 voice audio

Plays audio directly in the webpage

Uses secure environment variables for API key

Lightweight and beginner-friendly AI project

🔹 Technologies Used

Python

FastAPI

Google Gemini API

gTTS (Google Text-to-Speech)

HTML

python-dotenv

🔹 Project Structure
text-to-audio-ai/
│
├── main.py          # FastAPI application
├── .env             # Gemini API key (not uploaded to GitHub)
├── requirements.txt # Python dependencies
└── README.md        # Project documentation

🔹 Installation & Setup
create venv using
python -m venv venv
AND ACTIVATE
venv/SCripts/activate


2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Create .env file
GEMINI_API_KEY=your_api_key_here

🔹 Run the Project
uvicorn main:app --reload


Open in browser:

http://127.0.0.1:8000
