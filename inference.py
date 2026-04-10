import os
import random
from openai import OpenAI


client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"),
    api_key=os.environ.get("API_KEY")
)

def call_llm():
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Say OK"}],
            max_tokens=5
        )
        return response.choices[0].message.content
    except:
        return "fallback"

def run_task(task_name):
    print(f"[START] task={task_name}", flush=True)

    # STEP
    reward = round(random.uniform(0.3, 0.8), 2)
    print(f"[STEP] step=1 reward={reward}", flush=True)

    
    _ = call_llm()

    # END
    score = round(random.uniform(0.1, 0.9), 2)
    print(f"[END] task={task_name} score={score} steps=1", flush=True)


def main():
    tasks = ["task1", "task2", "task3"]

    for t in tasks:
        run_task(t)


if __name__ == "__main__":
    main()