from time import time
from datetime import datetime

class Note():
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
        return f"ID: {self.id}, created at {self.creation_date}\n{self._value}"