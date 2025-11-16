from src.handlers.input_error import input_error
from src.entities import NoteBook, Note

@input_error
def delete_note(args: list[str], _ , notes: NoteBook) -> str:
    """
    Remove note from NoteBook by id
    """
    note_id = int(args[0])
    if note_id in notes:
        notes.pop(note_id)
        return "Note deleted."
    return "Note with such id was not found."
