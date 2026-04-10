---
title: RL Warehouse Optimization
emoji: 🚀
colorFrom: blue
colorTo: purple
sdk: docker
app_file: inference.py
---

# RL Warehouse Optimization using LLM Evaluation

## Overview
This project simulates a reinforcement learning-based warehouse optimization system. 
Tasks such as path planning, obstacle avoidance, and multi-agent coordination are evaluated.

## Approach
- Each task simulates a warehouse optimization problem
- Reward is generated dynamically
- LLM is used for evaluation through provided proxy
- Structured outputs ensure validation compatibility

## Tasks
1. Path Planning
2. Obstacle Avoidance
3. Reward Optimization
4. Multi-Agent Coordination
5. Efficiency Analysis

## Scoring
Each task produces a score strictly between (0,1) ensuring valid evaluation.

## Tech Stack
- Python
- OpenAI API (via proxy)
- HuggingFace Spaces

## Key Highlight
Efficient integration of LLM-based evaluation with structured RL simulation.