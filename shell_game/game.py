import time
from state import GameState
from utils import colors

class Game:
    def __init__(self, questions):
        self.state = GameState()
        self.questions = questions

    def ask(self, q):
        while True:
            print(colors.info(q.prompt))
            answer = input("Komutunu yaz (İpucu için 'h'): ").strip()

            # İpucu sistemi
            if answer.lower() == "h" and q.hint:
                self.state.used_hints += 1
                self.state.add_score(-3)
                print(colors.warning(f"💡 İpucu: {q.hint} (-3 puan)"))
                continue

            # Cevap kontrolü (zaman ölçümü dahil)
            start = time.time()
            correct = q.check_answer(answer)
            duration = time.time() - start

            if correct:
                base = 10
                fast_bonus = 5 if duration <= 2.0 else 0
                self.state.add_score(base + fast_bonus)
                self.state.correct_answers += 1
                print(colors.success(f"✅ {q.success_msg} (+{base} puan)"))
                if fast_bonus:
                    print(colors.success(f"⚡ Hızlı cevap bonusu! (+{fast_bonus})"))
                if q.learn:
                    self.state.learned.append(q.learn)
                    print(colors.info(f"📘 Öğrendin: {q.learn}"))
                break
            else:
                self.state.lose_life()
                self.state.wrong_answers += 1
                print(colors.error(f"❌ {q.fail_msg} (-1 can)"))
                break

    def run(self):
        print(colors.info(">> Shell Game Başladı!"))
        for q in self.questions:
            if self.state.lives <= 0:
                print(colors.error("💀 Game Over!"))
                break
            self.ask(q)

        # Özet
        print(colors.info("\n=== Bölüm Özeti ==="))
        print(f"✅ Doğru: {self.state.correct_answers}")
        print(f"❌ Yanlış: {self.state.wrong_answers}")
        print(f"⭐ Puan: {self.state.score}")
        print(f"💡 Kullanılan ipucu: {self.state.used_hints}")
        if self.state.learned:
            print(colors.success("\n📘 Öğrendiklerin:"))
            for l in dict.fromkeys(self.state.learned):  # tekrarları engelle
                print(colors.success(f"- {l}"))
