from collections import UserDict
from src.entities.note import Note

class NoteBook(UserDict):
    """
    Class is for a set of notes, stored in data dict.
    Dictionary key is id of note, which is timestamp of creation
    """
    
    def add_note(self, note: Note) -> str:
        self[note.id] = note
