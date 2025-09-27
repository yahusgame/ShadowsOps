import time
from state import GameState
from utils import colors

class Game:
    def __init__(self, questions):
        self.state = GameState()
        self.questions = questions
    
    def ask(self, q):
        print(colors.info(q.prompt))
        answer = input("Komutunu yaz (İpucu için 'h'): ").strip()

        if answer.lower() == "h" and q.hint:
            self.state.used_hints += 1
            self.state.add_score(-3)
            print (colors.warning(f" İpucu: {q.hint} (-3 puan)"))
            return self.ask(q)
        if q.check_answer(answer):
            self.state.add_score(10)
            self.state.correct_answers += 1
            if q.learn:
                self.state.learned.append(q.learn)
            print(colors.success(f"{q.success_msg}"))
        else:
            self.state.lose_life()
            self.state.wrong_answers += 1
            print(colors.error(f"{q.fail_msg} (-1 can)"))
    def run(self):
        print(colors.info(">> Shell Game Başladı!"))
        for q in self.questions:
            if self.state.lives <= 0:
                print(colors.error("Game Over!"))
                break
            self.ask(q)
        print(colors.info("\n ==Bölüm Özeti=="))
        print(f"Doğru: {self.state.correct_answers}, Yanlış: {self.state.wrong_answers}, Puan: {self.state.score}")
        for l in self.state.learned:
            print(colors.success(f"- {l}"))