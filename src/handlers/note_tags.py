from src.handlers.input_error import input_error
from src.entities import NoteBook, Note

@input_error
def add_note_tag(args: list[str], _ , notes: NoteBook) -> str:
    """
    Add tag(-s) to note by its id
    """
    note_id = int(args[0])
    if not note_id in notes:
        return f"No such note found: {note_id} {notes}."
    for tag_name in args[1:]:
        if tag_name:
            notes[note_id].tags.append(tag_name)
    return "Tag(-s) added."

def remove_note_tag(args: list[str], _ , notes: NoteBook) -> str:
    """
    Remove tag(-s) from note by its id
    """
    note_id = int(args[0])
    if not note_id in notes:
        return f"No such note found: {note_id}."
    for tag_name in args[1:]:
        if tag_name in notes[note_id].tags:
            notes[note_id].tags.remove(tag_name)
    return "Tag(-s) removed."
