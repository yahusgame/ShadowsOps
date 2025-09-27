from loader import load_questions
from game import Game
import time

LEVELS = [
    "questions/level1.json",
    "questions/level2.json"
]

DEBUG_LEVEL = None  # Örn: 1 sadece Level 1, 2 sadece Level 2, None = normal oyun

def loading_screen(level_number):
    print(f"\n== Level {level_number} yükleniyor... ==")
    for i in range(3):
        print("." * (i + 1))
        time.sleep(0.7)
    print(f"\n== Level {level_number} Başlıyor! ==\n")

def main():
    if DEBUG_LEVEL:
        path = LEVELS[DEBUG_LEVEL - 1]
        loading_screen(DEBUG_LEVEL)
        questions = load_questions(path)
        game = Game(questions)
        game.run()
        return

    # Normal oyun akışı
    for i, level_path in enumerate(LEVELS, start=1):
        loading_screen(i)
        questions = load_questions(level_path)
        game = Game(questions)
        game.run()

        if game.state.lives <= 0:
            print("\n ❌ Oyunu Kaybettin. Tekrar dene!")
            break
        else:
            print(f"\n ✅ Level {i} Tamamlandı!")
            if i < len(LEVELS):
                print("⏭️  Sıradaki level yükleniyor...\n")
    else:
        print("\n 🎉 Tüm level'leri başarıyla bitirdin!")

if __name__ == "__main__":
    main()
