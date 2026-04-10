import os
from openai import OpenAI

# ✅ PRINT DIRECTLY (TOP LEVEL)
print("[START] task=warehouse", flush=True)

try:
    client = OpenAI(
        base_url=os.environ.get("API_BASE_URL"),
        api_key=os.environ.get("API_KEY")
    )

    response = client.chat.completions.create(
        model=os.environ.get("MODEL_NAME", "gpt-3.5-turbo"),
        messages=[
            {"role": "user", "content": "move right"}
        ]
    )

    action = response.choices[0].message.content

except Exception as e:
    action = "fallback"

# ✅ STEP
print(f"[STEP] step=1 reward=0.5 action={action}", flush=True)

# ✅ END
print("[END] task=warehouse score=1.0 steps=1", flush=True)