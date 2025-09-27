from dataclasses import dataclass
from typing import Optional, Union, List
import re

@dataclass
class Question:
    prompt: str
    correct: Union[str, List[str]]
    success_msg: str
    fail_msg: str
    hint: Optional[str] = None
    learn: Optional[str] = None
    narration_pre: Optional[str] = None
    narration_post: Optional[str] = None
    speaker: str = "mentor"

    def check_answer(self, answer: str) -> bool:
        ans = answer.strip().lower()

        if isinstance(self.correct, str) and self.correct.startswith("regex:"):
            pattern = self.correct[6:]
            return bool(re.fullmatch(pattern, ans))

        if isinstance(self.correct, list):
            return ans in [c.lower() for c in self.correct]

        return ans == self.correct.lower()

    def show_hint(self) -> Optional[str]:
        return f"💡 İpucu: {self.hint}" if self.hint else None
