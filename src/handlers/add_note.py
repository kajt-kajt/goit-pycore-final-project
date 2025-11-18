from src.handlers.input_error import input_error
from src.entities import NoteBook, Note

@input_error
def add_note(args: list[str], _ , notes: NoteBook) -> str:
    """
    Add note to NoteBook
    """
    note_text = args[0]
    note = Note(note_text)
    notes.add_note(note)
    return f"Note added. ID: {note.id}"