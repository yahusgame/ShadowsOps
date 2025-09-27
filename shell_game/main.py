from loader import load_questions
from game import Game

LEVELS = [
    "questions/level1.json",
    "questions/level2.json"
]

def main():
    for i, level_path in enumerate(LEVELS, start=1):
        print(f"\n ==Level {i} Başlıyor!==\n")
        questions = load_questions(level_path)
        game = Game(questions)
        game.run()

        if game.state.lives <= 0:
            print("\n Oyunu Kaybettin. Tekrar dene!")
            break
        else:
            print(f"\n Level {1} Tamamlandı!")
            if i < len(LEVELS):
                print("Sıradaki level yükleniyor...\n")
                
if __name__ == "__main__":
    main()