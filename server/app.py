from time import perf_counter

from fastapi import FastAPI
from pydantic import BaseModel, Field

from env.warehouse_env import WarehouseEnv

app = FastAPI(title="WarehouseRL Optimization API", version="1.0.0")
env = WarehouseEnv(size=7, max_steps=50, seed=42, stochasticity=0.0)
state = env.reset()


class Action(BaseModel):
    action: int = Field(ge=0, le=3, description="0=left, 1=right, 2=down, 3=up")


@app.get("/")
def home():
    return {"service": "warehouse-rl-optimization", "status": "ok", "version": "1.0.0"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/reset")
def reset():
    global state
    state = env.reset()
    return {"state": state, "goal": env.goal, "steps": env.steps}


@app.post("/step")
def step(action: Action):
    global state
    started = perf_counter()
    state, reward, done, _ = env.step(action.action)
    return {
        "state": state,
        "goal": tuple(env.goal),
        "reward": round(reward, 4),
        "done": done,
        "success": done and env.agent == env.goal,
        "steps": env.steps,
        "latency_ms": round((perf_counter() - started) * 1000, 3),
    }


@app.get("/state")
def get_state():
    return {"state": state, "goal": tuple(env.goal), "steps": env.steps}


def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)
