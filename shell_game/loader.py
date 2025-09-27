import json
from question import Question

def load_questions(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"[HATA] {path} bulunamadı.")
        return []
    except json.JSONDecodeError as e:
        print(f"[HATA] {path} JSON hatalı: {e}")
        return []

    questions = []
    for q in data:
        try:
            questions.append(Question(**q))
        except TypeError as e:
            print(f"[HATA] Geçersiz soru: {q} ({e})")
    print(f"[OK] {path} dosyasından {len(questions)} soru yüklendi.")
    return questions
