"""Small dependency-free inference helper for the warehouse environment."""


def greedy_action(state):
    """Choose an action that moves toward the goal in the compact state tuple."""
    x, y, goal_x, goal_y = state
    if x < goal_x:
        return 1
    if x > goal_x:
        return 0
    if y < goal_y:
        return 3
    return 2

