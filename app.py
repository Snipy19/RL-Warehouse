from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/run")
def run_model():
    return {"result": "RL executed"}