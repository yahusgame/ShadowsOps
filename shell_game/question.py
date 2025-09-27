from dataclasses import dataclass
from typing import Optional

@dataclass
class Question:
    prompt: str
    correct: str
    success_msg: str
    fail_msg: str
    hint: Optional[str] = None
    learn: Optional[str] = None

    def check_answer(self, answer: str) -> bool:
        return answer.strip() == self.correct