from src.handlers.input_error import input_error
from src.entities import AddressBook

@input_error
def show_email(args: list[str], contacts: AddressBook, _) -> str:
    """
    Returns email for given name.
    Returns an error message if contact with such name is absent.
    """
    name = args[0]
    return contacts[name].get_emails()
