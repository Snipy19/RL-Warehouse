---
emoji: 🚀
---

# WarehouseRL Optimization

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

WarehouseRL Optimization is a reproducible reinforcement learning project for warehouse robot navigation. It trains a tabular Q-learning agent, compares the learned policy with a random baseline, and exposes the environment through a production style FastAPI service.

The repository demonstrates measurable reinforcement learning performance, API integration, reproducible experiments, and container based deployment.

## Results

The benchmark evaluates 100 episodes for each task. The benchmark score is the average navigation efficiency for successful episodes:

```text
score = 1 - (steps / max_steps)
```

Latest local run:

| Task | Baseline success | Q-learning success | Reward improvement | Q-learning score | Inference latency |
| --- | ---: | ---: | ---: | ---: | ---: |
| Easy | 23% | 100% | +11.1729 | 0.7732 | 0.058 ms |
| Medium | 8% | 100% | +14.0295 | 0.7260 | 0.086 ms |
| Hard | 1% | 100% | +15.9764 | 0.6472 | 0.134 ms |

Mean Q-learning benchmark score: **0.7155** across **3 tasks**.

These are measurements from the local benchmark run included in this project. Run the benchmark again after changing the implementation or hardware.

## Features

- Tabular Q-learning with epsilon greedy exploration
- Easy, medium, and hard navigation environments
- Deterministic seeds for repeatable comparisons
- Random policy baseline for measuring improvement
- Success rate, reward, steps, benchmark score, and latency metrics
- FastAPI endpoints for environment interaction
- OpenAPI documentation through Swagger UI
- Docker deployment configuration
- Locked Python dependencies with `uv.lock`

## Architecture

```text
benchmark.py
    ├── trains QLearningAgent
    ├── evaluates random baseline
    └── reports reproducible metrics

env/warehouse_env.py
    └── grid navigation environment

server/app.py
    └── FastAPI service for reset, step, state, and health checks
```

For a detailed walkthrough and interview preparation, see [docs/INTERVIEW_GUIDE.md](docs/INTERVIEW_GUIDE.md).

## Requirements

- Python 3.10 or newer
- `uv` for the recommended workflow
- Docker, only if you want to run the container

## Installation

```powershell
git clone https://github.com/Snipy19/RL-Warehouse.git WarehouseRL-Optimization
cd WarehouseRL-Optimization
uv sync
```

The `uv sync` command creates the local virtual environment and installs the locked dependencies.

## Run the benchmark

```powershell
uv sync
uv run warehouse-benchmark
```

Or with an installed Python environment:

```powershell
python benchmark.py
```

The command prints JSON containing baseline and Q-learning success rates, average reward, average steps, benchmark score, improvement, inference latency, and the aggregate task score.

## Run the API locally

```powershell
uv run warehouse-api
```

The server listens on `http://localhost:7860`.

### API endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/health` | Service health check |
| `GET` | `/state` | Read current environment state |
| `POST` | `/reset` | Start a new episode |
| `POST` | `/step` | Apply an action |
| `GET` | `/docs` | Interactive API documentation |

Actions are integers from `0` to `3`:

```text
0 = left
1 = right
2 = down
3 = up
```

Example request:

```powershell
Invoke-RestMethod -Method Post `
  -Uri http://localhost:7860/step `
  -ContentType 'application/json' `
  -Body '{"action": 1}'
```

Each step response includes state, goal, reward, completion status, success status, step count, and server measured latency.

In a local 10-request API smoke run, all health and step requests returned HTTP 200. The mean measured step latency was 0.040 ms and the maximum was 0.066 ms.

## Deployment

The Dockerfile runs FastAPI with Uvicorn on port `7860`:

```powershell
docker build -t warehouserl-optimization .
docker run --rm -p 7860:7860 warehouserl-optimization
```

## Project structure

```text
.
├── agent/q_learning.py       # Q-learning agent
├── baseline/run.py           # Training entry point
├── env/                      # Environment, tasks, and metrics
├── server/app.py             # FastAPI service
├── benchmark.py              # Benchmark runner
├── Dockerfile                # Container deployment
├── pyproject.toml            # Package metadata and CLI commands
└── uv.lock                   # Locked dependencies
```

## Resume ready project summary

> Built a reproducible warehouse navigation simulator using tabular Q-learning, achieving a 0.7155 mean benchmark score and 100% success across three seeded task sizes; added baseline evaluation, latency measurement, FastAPI endpoints, and Docker deployment support.

## Scope and limitations

This is a simulated grid navigation benchmark. It does not represent a production warehouse layout, real robot sensor stack, physical motion planner, or multi robot fleet controller. The reported results describe this simulation and should be presented with that context.

## License

This project is released under the MIT License.
