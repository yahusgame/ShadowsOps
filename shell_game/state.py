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
        """Skora puan ekler, negatif olmamasını sağlar."""
        self.score = max(0, self.score + points)

    def lose_life(self):
        """Can kaybı, 0’ın altına düşmez."""
        if self.lives > 0:
            self.lives -= 1

    def reset(self):
        """Yeni oyun için state sıfırla."""
        self.lives = 3
        self.score = 0
        self.used_hints = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.learned.clear()

    def summary(self) -> str:
        """Durumun özetini döndürür (string)."""
        summary_lines = [
            f"✅ Doğru: {self.correct_answers}",
            f"❌ Yanlış: {self.wrong_answers}",
            f"⭐ Puan: {self.score}",
            f"💡 Kullanılan ipucu: {self.used_hints}"
        ]
        if self.learned:
            summary_lines.append("\n📘 Öğrendiklerin:")
            for item in dict.fromkeys(self.learned):  # tekrarları engelle
                summary_lines.append(f"- {item}")
        return "\n".join(summary_lines)
