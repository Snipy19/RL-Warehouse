import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ["API_BASE_URL"],  # ✅ MUST
    api_key=os.environ["API_KEY"]         # ✅ MUST
)

def run_llm():
    response = client.chat.completions.create(
        model=os.environ.get("MODEL_NAME", "gpt-3.5-turbo"),
        messages=[
            {"role": "user", "content": "move right"}
        ]
    )
    return response.choices[0].message.content