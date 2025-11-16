from src.handlers.input_error import input_error
from src.entities import NoteBook

@input_error
def show_all_notes(args: list[str], _ , notes: NoteBook) -> str:
    """
    Display all notes from NoteBook
    """
    return "\n\n".join([str(note) for note in notes.data.values()]) + "\n"
