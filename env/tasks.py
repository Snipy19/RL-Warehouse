import random
from env.warehouse_env import WarehouseEnv

def easy_task():
    return WarehouseEnv(size=5, max_steps=40, seed=random.randint(0,1000))

def medium_task():
    return WarehouseEnv(size=7, max_steps=50, seed=random.randint(0,1000))

def hard_task():
    return WarehouseEnv(size=10, max_steps=60, seed=random.randint(0,1000))