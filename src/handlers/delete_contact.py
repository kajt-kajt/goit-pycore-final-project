from src.handlers.input_error import input_error
from src.entities import AddressBook


@input_error
def delete_contact(args: list[str], contacts: AddressBook) -> str:
    """
    Remove entire contact record by name.
    """
    name = args[0]
    if name not in contacts:
        return f"ERROR: contact '{name}' does not exist!"
    contacts.pop(name)
    return "Contact deleted."
