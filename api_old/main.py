from fastapi import FastAPI
from env.tasks import easy_task

app = FastAPI()

env = easy_task()

@app.get("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(action: int):
    state, reward, done, _ = env.step(action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }

@app.get("/state")
def state():
    return {"state": env._get_state()}