from dataclasses import dataclass, field
from typing import List

@dataclass
class GameState:
    lives: int = 3
    score: int = 0
    used_hints: int = 0
    correct_answers: int = 0
    wrong_answers: int = 0
    learned: List[str] = field(default_factory=list)

    def add_score(self, points: int):
        self.score = max(0, self.score + points)

    def lose_life(self):
        if self.lives > 0:
            self.lives -= 1

    def reset(self):
        self.__init__()

    def summary(self) -> str:
        lines = [
            f"✅ Doğru: {self.correct_answers}",
            f"❌ Yanlış: {self.wrong_answers}",
            f"⭐ Puan: {self.score}",
            f"💡 Kullanılan ipucu: {self.used_hints}"
        ]
        if self.learned:
            lines.append("\n📘 Öğrendiklerin:")
            for item in dict.fromkeys(self.learned):
                lines.append(f"- {item}")
        return "\n".join(lines)
