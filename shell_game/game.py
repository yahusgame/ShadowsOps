import time
from state import GameState
from utils import colors

class Game:
    def __init__(self, questions):
        self.state = GameState()
        self.questions = questions

    def _narrate(self, text, speaker="mentor"):
        if not text:
            return
        if speaker == "hacker":
            print(colors.hacker(f"🕶️ {text}"))
        else:
            print(colors.mentor(f"🧭 {text}"))

    def ask(self, q):
        self._narrate(q.narration_pre, q.speaker)

        print(colors.prompt(q.prompt))
        answer = input("👉 Komutunu yaz (İpucu için 'h'): ").strip()

        if answer.lower() == "h" and q.hint:
            self.state.used_hints += 1
            self.state.add_score(-3)
            print(colors.hint(q.show_hint()))
            return self.ask(q)

        correct = q.check_answer(answer)

        if correct:
            self.state.add_score(10)
            self.state.correct_answers += 1
            print(colors.success(q.success_msg))
            self._narrate(q.narration_post, q.speaker)
        else:
            self.state.lose_life()
            self.state.wrong_answers += 1
            print(colors.error(f"{q.fail_msg}  ❤️ -1 Can"))

        print(self.state.status_bar())  # can, puan, ipucu göster

    def run(self):
        print(colors.info(">> Shell Game Başladı!"))
        for q in self.questions:
            if self.state.lives <= 0:
                print(colors.error("💀 Game Over!"))
                break
            self.ask(q)

        print(colors.info("\n=== Bölüm Özeti ==="))
        print(self.state.summary())
