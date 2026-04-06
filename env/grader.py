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

            if done and reward > 0:
                success = True

        # efficiency-based scoring (KEY)
        if success:
            efficiency = max(0, 1 - (steps / env.max_steps))
            total_score += efficiency
        else:
            total_score += 0

    return round(total_score / episodes, 3)