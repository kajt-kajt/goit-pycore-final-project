from src.handlers.input_error import input_error
from src.entities import AddressBook


@input_error
def delete_address(args: list[str], contacts: AddressBook) -> str:
    """
    Removes the address from the contact.
    """
    name = args[0]
    if name not in contacts:
        return f"ERROR: contact '{name}' does not exist!"
    record = contacts[name]
    if record.get_address():
        record.add_address(None)
        return "Address deleted."
    return "Nothing to delete."
