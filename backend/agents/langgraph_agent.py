from groq import Groq
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)


def run_agent(message: str):

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant helping pharmaceutical sales representatives log interactions with Healthcare Professionals (HCPs). Summarize the interaction clearly."
            },
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=0.3,
        max_tokens=200
    )

    response = completion.choices[0].message.content

    return {
        "message": response
    }