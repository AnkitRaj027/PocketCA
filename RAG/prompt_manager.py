from pathlib import Path

from rag.config import ROOT_DIR


class PromptManager:
    """
    Loads prompt templates from disk.
    """

    PROMPT_DIR = ROOT_DIR / "rag" / "prompts"

    @classmethod
    def load(cls, filename: str) -> str:
        """
        Load a prompt file.

        Args:
            filename: Name of the prompt file.

        Returns:
            Prompt text.
        """

        path = cls.PROMPT_DIR / filename

        return path.read_text(
            encoding="utf-8"
        )