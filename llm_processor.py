from dotenv import load_dotenv
from groq import Groq

load_dotenv()
groq = Groq()

def classify_with_llm(log_message):
    prompt = f'''Classify the log message into one of these two categories:
    (1) Workflow Error, (2) Deprecation Warning.
    If you cant figure it out, return "Unclassified".
    Only return category name. No preamble.
    Log message: {log_message}'''


    chat_completions = groq.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages=[
            {
                "role" : "user",
                "content" : prompt,
            }
        ]
    )

    return chat_completions.choices[0].message.content