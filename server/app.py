from fastapi import FastAPI
from pydantic import BaseModel
from inference import run_llm

app = FastAPI()

state = {"position": 0}

class Action(BaseModel):
    action: int

@app.get("/")
def home():
    return {"status": "RUNNING OK"}

@app.post("/reset")
def reset():
    global state
    state = {"position": 0}
    return {"state": state}

@app.post("/step")
def step(action: Action):
    global state

    
    llm_output = run_llm()

    state["position"] += action.action

    reward = 1 if state["position"] > 5 else 0
    done = state["position"] > 10

    return {
        "state": state,
        "reward": reward,
        "done": done,
        "llm": llm_output
    }

@app.get("/state")
def get_state():
    return state


def main():
    return app


if __name__ == "__main__":
    main()