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
        self.score += points
    
    def lose_life(self):
        self.lives -= 1