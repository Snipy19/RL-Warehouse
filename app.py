print("🔥 APP.PY RUNNING")

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"status": "RUNNING OK"}

@app.get("/run")
def run():
    return {"msg": "WORKING"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)