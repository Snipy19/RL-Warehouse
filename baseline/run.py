from env.tasks import easy_task, medium_task, hard_task
from env.grader import evaluate
from agent.q_learning import QLearningAgent


def train(env, episodes):
    agent = QLearningAgent()

    for ep in range(episodes):
        state = env.reset()
        done = False

        while not done:
            action = agent.get_action(state)
            next_state, reward, done, _ = env.step(action)

            agent.update(state, action, reward, next_state)
            state = next_state

        agent.decay()

    return agent


def run():
    tasks = {
        "easy": easy_task(),
        "medium": medium_task(),
        "hard": hard_task()
    }

    results = {}

    for name, env in tasks.items():
        print(f"Training on {name} task...")

        # balanced training
        episodes = 800 if name == "easy" else 1200 if name == "medium" else 2000

        agent = train(env, episodes)

        # evaluation without exploration
        old_epsilon = agent.epsilon
        agent.epsilon = 0.0

        score = evaluate(env, agent.get_action)

        agent.epsilon = old_epsilon

        results[name] = round(score, 3)
        print(f"{name} score: {results[name]}")

    return results


if __name__ == "__main__":
    final_results = run()
    print("\nFinal Results:")
    print(final_results)