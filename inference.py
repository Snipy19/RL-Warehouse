import os
from openai import OpenAI
from env.tasks import easy_task, medium_task, hard_task
from env.grader import evaluate
from agent.q_learning import QLearningAgent


client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("HF_TOKEN"),
)

MODEL = os.getenv("MODEL_NAME")
def llm_decision(state):
    prompt = f"Agent is at {state[:2]} and goal is {state[2:]}. Choose action (0=up,1=down,2=left,3=right)."

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=5
    )

    text = response.choices[0].message.content.strip()

    # fallback parsing
    for i in range(4):
        if str(i) in text:
            return i

    return 0


def run_task(name, env):
    print(f"[START] task={name}")

    agent = QLearningAgent()

    for _ in range(300):
        state = env.reset()
        done = False

        while not done:
            action = agent.get_action(state)
            next_state, reward, done, _ = env.step(action)
            agent.update(state, action, reward, next_state)
            state = next_state

        agent.decay()

    agent.epsilon = 0.0
    score = evaluate(env, agent.get_action)

    print(f"[END] task={name} score={round(score,3)}")
    return score


def main():
    tasks = {
        "easy": easy_task(),
        "medium": medium_task(),
        "hard": hard_task()
    }

    results = {}

    for name, env in tasks.items():
        results[name] = run_task(name, env)

    print(results)


if __name__ == "__main__":
    main()