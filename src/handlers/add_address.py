from src.handlers.input_error import input_error
from src.entities import AddressBook, Record

@input_error
def add_address(args: list[str], contacts: AddressBook) -> str:
    """
    Adds address to contacts book object. 
    If contact with such name already exists, updates address for that user.
    "args" should contain 2 values.
    """
    name, address = args
    ## if contact already exists, adding one more email for user
    if not name in contacts:
        contacts[name] = Record(name)
    contacts[name].add_address(address)
    return "Address added."
