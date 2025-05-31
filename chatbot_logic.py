import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def handle_message(msg):
    if "course" in msg.lower():
        return "Here's the LMS dashboard: https://your-lms-site.com"
    elif "payment" in msg.lower():
        return "You can view your receipts at https://your-lms-site.com/billing"
    else:
        return ai_response(msg)

def ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
