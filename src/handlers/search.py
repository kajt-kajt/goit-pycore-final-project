from src.handlers.input_error import input_error
from src.entities import AddressBook, NoteBook

@input_error
def search_contacts(args: list[str], contacts: AddressBook, _) -> str:
    """
    Search all fields for AddressBook for substring
    """
    pattern = args[0]
    return contacts.search_by_pattern(pattern)

@input_error
def search_notes(args: list[str], _, notes: NoteBook) -> str:
    """
    Search all notes of NoteBook for substring
    """
    pattern = args[0]
    return notes.search_by_pattern(pattern)

@input_error
def search_books(args: list[str], contacts: AddressBook, notes: NoteBook) -> str:
    """
    Search both address book and note book for a pattern
    """
    pattern = args[0]
    contacts_result = contacts.search_by_pattern(pattern)
    notes_result = notes.search_by_pattern(pattern)
    if notes_result:
        notes_result = "Match in notes:\n\n" + notes_result
    delimiter = ""
    if notes_result and contacts_result:
        delimiter = "\n" + "-"*20 + "\n"
    return f"{contacts_result}{delimiter}{notes_result}"
