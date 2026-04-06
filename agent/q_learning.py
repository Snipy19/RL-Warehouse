import numpy as np
import random
from collections import defaultdict

class QLearningAgent:
    def __init__(self, actions=4):
        self.q = defaultdict(lambda: np.zeros(actions))
        self.alpha = 0.2
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_decay = 0.995
        self.epsilon_min = 0.05

    def get_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, 3)
        return int(np.argmax(self.q[state]))

    def update(self, state, action, reward, next_state):
        best_next = np.max(self.q[next_state])
        self.q[state][action] += self.alpha * (
            reward + self.gamma * best_next - self.q[state][action]
        )

    def decay(self):
        self.epsilon = max(self.epsilon_min, self.epsilon * self.epsilon_decay)