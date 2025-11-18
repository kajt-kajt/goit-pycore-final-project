from time import time
from datetime import datetime


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
        tag_line = " #".join(self.tags)
        if tag_line:
            tag_line = "\n   #" + tag_line
        return (
            f"ID: {self.id}, created at {self.creation_date}\n"
            f"{self._value}{tag_line}"
        )
    
    def search_by_pattern(self, pattern:str) -> str:
        """
        Search note text by substring
        """
        pattern_sanitized = pattern.casefold()
        if pattern_sanitized in self._value.casefold():
            return str(self)
        return ""

