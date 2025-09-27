from loader import load_questions
from game import Game

LEVELS = [
    "questions/level1.json",
    "questions/level2.json"
]

def run_level(level_number, level_path):
    print(f"\n== Level {level_number} Başlıyor! ==\n")
    try:
        questions = load_questions(level_path)
    except FileNotFoundError:
        print(f"Hata: {level_path} bulunamadı!")
        return False
    
    game = Game(questions)
    game.run()

    if game.state.lives <= 0:
        print("\n Oyunu Kaybettin. Tekrar dene!")
        return False
    else:
        print(f"\n Level {level_number} Tamamlandı!")
        return True

def main():
    for i, level_path in enumerate(LEVELS, start=1):
        if not run_level(i, level_path):
            break
        if i < len(LEVELS):
            print("Sıradaki level yükleniyor...\n")
    else:
        print("\n 🎉 Tüm level'leri başarıyla bitirdin!")

if __name__ == "__main__":
    main()
