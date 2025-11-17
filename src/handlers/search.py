from src.handlers.input_error import input_error
from src.entities import AddressBook

@input_error
def search_contacts(args: list[str], contacts: AddressBook, _) -> str:
    """
    Search all fields for AddressBook for substring
    """
    pattern = args[0]
    return contacts.search_by_pattern(pattern)
