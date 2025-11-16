from src.entities import AddressBook
from src.handlers.input_error import input_error

def show_all(_, contacts: AddressBook) -> str:
    """
    Outputs all the contents of in-memory database of contacts.
    """
    result = [f"{contacts[name]}" for name in contacts]
    return "\n".join(result)

@input_error
def show_contact(args: list[str], contacts: AddressBook) -> str:
    """
    Outputs all the contents of in-memory database of contacts.
    """
    name = args[0]
    result = f"{contacts[name]}"
    return result
