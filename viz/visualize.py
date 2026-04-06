import matplotlib.pyplot as plt
from env.tasks import easy_task

env = easy_task()
state = env.reset()

grid = [[0]*env.size for _ in range(env.size)]
ax, ay = env.agent
gx, gy = env.goal

grid[ax][ay] = 1
grid[gx][gy] = 2

plt.imshow(grid)
plt.title("Warehouse")
plt.show()