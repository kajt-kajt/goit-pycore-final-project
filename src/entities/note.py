from time import time
from datetime import datetime
from colorama import Fore, Style


class Note:
    """
    Class represents a single note entity
    """

    def __init__(self, value):
        super().__init__()
        self._value = value
        self.id = int(time())
        self.creation_date = datetime.now().strftime("%Y-%m-%d_%H:%M")
        self.tags = []

    def __str__(self):
        header = (
            f"{Fore.LIGHTBLACK_EX}ID: {self.id}, created at {self.creation_date}"
            f"{Style.RESET_ALL}"
        )

        tag_line = ""
        if self.tags:
            tags = " #".join(self.tags)
            tag_line = f"\n{Fore.LIGHTBLACK_EX}   #{tags}{Style.RESET_ALL}"

        note_text = f"{Fore.CYAN}{self._value}{Style.RESET_ALL}"

        return f"{header}\n{note_text}{tag_line}"
    
    def search_by_pattern(self, pattern:str) -> str:
        """
        Search note text by substring
        """
        pattern_sanitized = pattern.casefold()
        if pattern_sanitized in self._value.casefold():
            return str(self)
        return ""

