import os
import json

DATA_PATH = "data/tasks.json"

def save_tasks(task_list):
    os.makedirs("data", exist_ok=True)
    try:
        with open(DATA_PATH, "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

    tasks.extend(task_list)
    with open(DATA_PATH, "w") as f:
        json.dump(tasks, f, indent=2)

def load_tasks():
    try:
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
