from dataclasses import dataclass
from typing import Optional, Union, List
import re

@dataclass
class Question:
    prompt: str
    correct: Union[str, List[str]]  # hem tek string hem liste olabilir
    success_msg: str
    fail_msg: str
    hint: Optional[str] = None
    learn: Optional[str] = None

    def check_answer(self, answer: str) -> bool:
        ans = answer.strip().lower()

        # Regex desteği
        if isinstance(self.correct, str) and self.correct.startswith("regex:"):
            pattern = self.correct[6:]
            return bool(re.fullmatch(pattern, ans))

        # Çoklu doğru cevap desteği
        if isinstance(self.correct, list):
            return ans in [c.lower() for c in self.correct]

        # Normal tekli cevap
        return ans == self.correct.lower()

    def show_hint(self) -> Optional[str]:
        """İpucu varsa formatlı string döndürür."""
        return f"💡 İpucu: {self.hint}" if self.hint else None

    def show_learn(self) -> Optional[str]:
        """Öğrenme çıktısı varsa formatlı string döndürür."""
        return f"📘 Öğrendin: {self.learn}" if self.learn else None
