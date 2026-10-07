from openai import OpenAI
import os
from dotenv import load_dotenv
from app.prompts import EXTRACT_CANDIDATE_DETAILS
import json

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def extract_resume_data(resume_text):
    prompt = EXTRACT_CANDIDATE_DETAILS.format(resume_text=resume_text)
    try:
        response = client.chat.completions.create(
            model = "gpt-4",
            messages = [
                {
                    "role": "system",
                    "content": prompt
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return {"error": str(e)}