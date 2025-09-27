import json
from question import Question

def load_questions(path: str):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return[Question(**q) for q in data]