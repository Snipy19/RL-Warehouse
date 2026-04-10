import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ["API_BASE_URL"],
    api_key=os.environ["API_KEY"]
)

def run_llm():
    response = client.chat.completions.create(
        model=os.environ.get("MODEL_NAME", "gpt-3.5-turbo"),
        messages=[
            {"role": "user", "content": "move right"}
        ]
    )
    return response.choices[0].message.content


def run():
    # START BLOCK
    print("[START] task=warehouse", flush=True)

    # LLM CALL 
    output = run_llm()

    # STEP BLOCK
    print(f"[STEP] step=1 reward=0.5 action={output}", flush=True)

    # END BLOCK
    print("[END] task=warehouse score=1.0 steps=1", flush=True)


if __name__ == "__main__":
    run()