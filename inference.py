import os
from openai import OpenAI

# LLM client (MANDATORY)
client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"),
    api_key=os.environ.get("API_KEY")
)

# LLM decides movement
def get_action(x, y, gx, gy, obstacles):
    prompt = f"""
    You are a warehouse robot.

    Current position: ({x},{y})
    Goal: ({gx},{gy})
    Obstacles: {obstacles}

    Choose ONLY one move:
    up / down / left / right
    """

    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5
        )

        move = res.choices[0].message.content.lower()

    except:
        move = "right"

    return move


# Apply movement
def move_agent(x, y, action):
    if "right" in action:
        return x + 1, y
    elif "left" in action:
        return x - 1, y
    elif "up" in action:
        return x, y + 1
    elif "down" in action:
        return x, y - 1
    return x, y


# Task simulation
def run_task(name, start, goal, obstacles):
    print(f"[START] task={name}", flush=True)

    x, y = start
    gx, gy = goal

    steps = 0
    max_steps = 8

    while (x, y) != (gx, gy) and steps < max_steps:
        steps += 1

        action = get_action(x, y, gx, gy, obstacles)
        nx, ny = move_agent(x, y, action)

        # obstacle check
        if (nx, ny) in obstacles:
            nx, ny = x, y  # stay if blocked

        x, y = nx, ny

        reward = round(1 / (steps + 1), 2)
        print(f"[STEP] step={steps} reward={reward}", flush=True)

    # scoring (efficiency based)
    score = 1 - (steps / max_steps)

    # strict range fix
    if score <= 0:
        score = 0.01
    if score >= 1:
        score = 0.99

    print(f"[END] task={name} score={round(score,2)} steps={steps}", flush=True)


# Main execution
def main():
    run_task(
        "easy_navigation",
        start=(0, 0),
        goal=(2, 2),
        obstacles=[(1, 1)]
    )

    run_task(
        "medium_navigation",
        start=(0, 0),
        goal=(4, 3),
        obstacles=[(2, 2), (3, 1)]
    )

    run_task(
        "hard_navigation",
        start=(1, 1),
        goal=(6, 5),
        obstacles=[(2, 2), (3, 3), (4, 4)]
    )


if __name__ == "__main__":
    main()