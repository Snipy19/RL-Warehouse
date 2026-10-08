"""Run a reproducible baseline versus Q-learning benchmark."""

import json
import random
import statistics
import time

from agent.q_learning import QLearningAgent
from env.grader import evaluate_detailed
from env.tasks import easy_task, hard_task, medium_task


def train(env, episodes):
    agent = QLearningAgent()
    for _ in range(episodes):
        state = env.reset()
        done = False
        while not done:
            action = agent.get_action(state)
            next_state, reward, done, _ = env.step(action)
            agent.update(state, action, reward, next_state)
            state = next_state
        agent.decay()
    agent.epsilon = 0.0
    return agent


def random_policy(_state):
    return random.randint(0, 3)


def measure(policy, env, episodes=100):
    started = time.perf_counter()
    metrics = evaluate_detailed(env, policy, episodes)
    metrics["inference_latency_ms"] = round((time.perf_counter() - started) * 1000 / episodes, 3)
    return metrics


def main():
    random.seed(7)
    tasks = {"easy": (easy_task, 800), "medium": (medium_task, 1200), "hard": (hard_task, 2000)}
    report = {"project": "WarehouseRL Optimization", "episodes": 100, "tasks": {}}
    for name, (factory, training_episodes) in tasks.items():
        baseline = measure(random_policy, factory())
        agent = train(factory(), training_episodes)
        learned = measure(agent.get_action, factory())
        learned["reward_improvement"] = round(learned["average_reward"] - baseline["average_reward"], 4)
        learned["success_rate_improvement"] = round(learned["success_rate"] - baseline["success_rate"], 4)
        report["tasks"][name] = {"baseline": baseline, "q_learning": learned}
    scores = [item["q_learning"]["benchmark_score"] for item in report["tasks"].values()]
    report["summary"] = {
        "task_count": len(report["tasks"]),
        "mean_benchmark_score": round(statistics.mean(scores), 4),
        "deployment": "FastAPI + Uvicorn; Dockerfile included",
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
