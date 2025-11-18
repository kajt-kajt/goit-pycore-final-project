from src.handlers.input_error import input_error
from src.entities import NoteBook, Note

@input_error
def add_note(args: list[str], _, notes: NoteBook) -> str:
    """
    Add note to NoteBook, supporting tags: #tag
    """
    if not args:
        return "Please provide note text."

    note_text = args[0]
    raw_tags = args[1:]

    # фільтруємо тільки ті, що починаються на #
    tags = [t[1:] for t in raw_tags if t.startswith("#")]

    note = Note(note_text, tags=tags)
    note_id = notes.add_note(note)

    if tags:
        return f"Note added. ID: {note_id}. Tags: {', '.join(tags)}"
    else:
        return f"Note added. ID: {note_id}."
