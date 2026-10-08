from env.warehouse_env import WarehouseEnv

def easy_task():
    return WarehouseEnv(size=5, max_steps=40, seed=101)

def medium_task():
    return WarehouseEnv(size=7, max_steps=50, seed=202)

def hard_task():
    return WarehouseEnv(size=10, max_steps=60, seed=303)
