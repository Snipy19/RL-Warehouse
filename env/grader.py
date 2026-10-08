def evaluate(env, policy, episodes=10):
    total_score = 0

    for _ in range(episodes):
        state = env.reset()
        done = False
        steps = 0
        success = False

        while not done:
            action = policy(state)
            state, reward, done, _ = env.step(action)
            steps += 1

            if done and env.agent == env.goal:
                success = True

        # efficiency-based scoring (KEY)
        if success:
            efficiency = max(0, 1 - (steps / env.max_steps))
            total_score += efficiency
        else:
            total_score += 0

    return round(total_score / episodes, 3)


def evaluate_detailed(env, policy, episodes=100):
    """Return reproducible success, reward, steps, and score measurements."""
    total_reward = 0.0
    total_steps = 0
    total_score = 0.0
    successes = 0
    for _ in range(episodes):
        state = env.reset()
        done = False
        episode_reward = 0.0
        steps = 0
        while not done:
            state, reward, done, _ = env.step(policy(state))
            episode_reward += reward
            steps += 1
        success = env.agent == env.goal
        successes += int(success)
        total_reward += episode_reward
        total_steps += steps
        if success:
            total_score += max(0.0, 1 - steps / env.max_steps)
    return {
        "success_rate": round(successes / episodes, 4),
        "average_reward": round(total_reward / episodes, 4),
        "average_steps": round(total_steps / episodes, 2),
        "benchmark_score": round(total_score / episodes, 4),
    }
