from src.handlers.input_error import input_error
from src.entities import NoteBook


@input_error
def add_note(args: list[str], _, notes: NoteBook) -> str:
    """
    Add note to NoteBook and return its ID
    """
    note_text = args[0]
    note_id = notes.add_note_text(note_text)  # якщо створення переносимо в NoteBook
    return f"Note added. ID: {note_id}"


@input_error
def add_note_with_tags(args: list[str], _, notes: NoteBook) -> str:
    """
    Add note and tags in format: note_text #tag1 #tag2
    """
    if not args:
        return "Please provide note text."

    note_text = args[0]
    tags = [t[1:] for t in args[1:] if t.startswith("#")]

    note_id = notes.add_note_text(note_text, tags=tags)

    if tags:
        return f"Note added. ID: {note_id}. Tags: {', '.join(tags)}"
    return f"Note added. ID: {note_id}"


@input_error
def delete_note(args: list[str], _, notes: NoteBook) -> str:
    """
    Delete note by ID
    """
    note_id = int(args[0])
    notes.delete_note(note_id)
    return f"Note {note_id} deleted."


@input_error
def edit_note(args: list[str], _, notes: NoteBook) -> str:
    """
    Edit note text by ID
    """
    note_id = int(args[0])
    new_text = args[1]
    notes.edit_note(note_id, new_text)
    return f"Note {note_id} updated."


@input_error
def add_tag(args: list[str], _, notes: NoteBook) -> str:
    """
    Add tag to note by ID
    """
    note_id = int(args[0])
    tag = args[1]
    notes.add_tag(note_id, tag)
    return f"Tag '{tag}' added to note {note_id}."
