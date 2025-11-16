from src.handlers.input_error import input_error
from src.entities import AddressBook


@input_error
def change_email(args: list[str], contacts: AddressBook) -> str:
    """
    Replace an existing email for a contact with a new value.
    """
    name, old_email, new_email = args
    if name not in contacts:
        return f"ERROR: contact '{name}' does not exist!"
    updated = contacts[name].edit_email(old_email, new_email)
    return "Email updated." if updated else "Nothing to change."
