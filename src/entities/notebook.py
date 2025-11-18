from collections import UserDict
from src.entities.note import Note

class NoteBook(UserDict):
    """
    Class is for a set of notes, stored in data dict.
    Dictionary key is id of note, which is timestamp of creation
    """

    def create(self, text, tags=None):
        note = Note(text, tags=tags)
        self[note.id] = note
        return note.id

    def add_note(self, note: Note) -> str:
        self[note.id] = note
        return note.id

    def search_by_pattern(self, pattern: str) -> str:
        """
        Search all notes for a match of a pattern
        """
        results = [note.search_by_pattern(pattern) for note in self.values()]
        return "\n\n".join([value for value in results if value])
