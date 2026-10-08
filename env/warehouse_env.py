import random

class WarehouseEnv:
    def __init__(self, size=7, max_steps=60, seed=None, stochasticity=0.15):
        self.size = size
        self.max_steps = max_steps
        self.stochasticity = stochasticity
        self.rng = random.Random(seed)

    def reset(self):
        self.agent = [0, 0]
        self.goal = [self.size - 1, self.size - 1]
        self.steps = 0

        return self._get_state()

    def _get_state(self):
        return tuple(self.agent + self.goal)

    def step(self, action):
        self.steps += 1

        moves = {0: (-1,0), 1:(1,0), 2:(0,-1), 3:(0,1)}

        # stochastic action (KEY)
        if self.rng.random() < self.stochasticity:
            action = self.rng.randint(0, 3)

        dx, dy = moves[action]
        new_pos = [self.agent[0] + dx, self.agent[1] + dy]

        old_dist = abs(self.agent[0]-self.goal[0]) + abs(self.agent[1]-self.goal[1])

        # valid move
        if 0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size:
            self.agent = new_pos

        new_dist = abs(self.agent[0]-self.goal[0]) + abs(self.agent[1]-self.goal[1])

        # reward shaping
        reward = -0.1 + (old_dist - new_dist) * 0.2

        # small randomness
        reward += self.rng.uniform(-0.05, 0.05)

        done = False

        if self.agent == self.goal:
            reward += 8   # not too large
            done = True

        if self.steps >= self.max_steps:
            reward -= 2
            done = True

        return self._get_state(), reward, done, {}
