from time import time
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

class Note:
    """
    Class represents a single note entity
    """

    def __init__(self, value):
        super().__init__()
        self._value = value
        self.id = int(time())
        self.creation_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.tags = []

    def __str__(self):
        # Grey color for meta info and tags
        meta = f"{Fore.CYAN}ID: {self.id}{Style.RESET_ALL}  {Fore.LIGHTBLACK_EX}{self.creation_date}{Style.RESET_ALL}"

        # Main text stays standard (white/default)
        text = f"{self._value}"

        # Tags in grey
        if self.tags:
            tags = "  ".join(f"#{t}" for t in self.tags)
            tag_line = f"\n   {Fore.LIGHTBLACK_EX}{tags}{Style.RESET_ALL}"
        else:
            tag_line = ""

        return f"{meta}\n{text}{tag_line}"

    def search_by_pattern(self, pattern: str) -> str:
        """
        Search note text by substring
        """
        pattern_sanitized = pattern.casefold()
        if pattern_sanitized in self._value.casefold():
            return str(self)
        return ""
