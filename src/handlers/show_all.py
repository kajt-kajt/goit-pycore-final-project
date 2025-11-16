from src.entities import AddressBook

def show_all(_, contacts: AddressBook) -> str:
    """
    Outputs all the contents of in-memory database of contacts.
    """
    result = [f"{contacts[name]}" for name in contacts]
    return "\n".join(result)

def show_names(_, contacts: AddressBook) -> dict:
    """
    Show names of all available contacts
    """
    return [{"Name": name} for name in contacts.keys()]

def show_field(args: list[str], contacts: AddressBook) -> str:
    """
    Shows particular field
    """
    pass