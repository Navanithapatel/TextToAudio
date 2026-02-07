import os
import uuid
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
import google.generativeai as genai
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI KEY is empty")
genai.configure(api_key=API_KEY)
app = FastAPI()

#GET- Show text input  from
@app.get("/", response_class=HTMLResponse)
async def text_from():
    return f"""
    <html>
       <body>
          <h2>Text to Audio</h2>
          <form action="/result" method="post">
             <textarea name="text" rows="5" cols="50" required></textarea><br>
          <input type="submit" value="Generate Audio">
          </form>
        </body>
    </html>
"""

#POST - process text
@app.post("/result", response_class=HTMLResponse)
async def result(text: str = Form(...)):
    #step1:generate text using Gemini
    model = genai.GenerativeModel("gemini-flash-latest")
    response = model.generate_content(text)
    generated_text = response.text

    #step2: Convert to audio
    filename = f"{uuid.uuid4().hex}.mp3"
    tts = gTTS(generated_text, lang="en")
    tts.save(filename)

    #step:3
    return f"""
    <html>
       <body>
          <h2>Generated Text</h2>
          <p>{generated_text}</p>
          <h2>Audio Output</h2>
          <audio controls>
              <source src="/audio/{filename}" type="audio/mpeg">
          </audio> <br>
          <a href="/">Back</a>          
        </body>
    </html>
"""

# Audio file route
@app.get("/audio/{filename}")
async def audio(filename: str):
    return FileResponse(path=filename, media_type="audio/mpeg", filename=filename)