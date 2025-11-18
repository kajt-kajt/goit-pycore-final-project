from src.handlers.input_error import input_error
from src.entities import AddressBook


@input_error
def delete_phone(args: list[str], contacts: AddressBook, _) -> str:
    """
    Removes a phone number from the contact.
    If phone is not provided and only one exists, it will be removed.
    """
    if not args:
        raise ValueError("No arguments provided.")

    name, *rest = args
    if name not in contacts:
        return f"ERROR: contact '{name}' does not exist!"

    record = contacts[name]
    phone_to_remove = rest[0] if rest else None

    if phone_to_remove is None:
        if len(record.phones) == 1:
            phone_to_remove = str(record.phones[0])
        else:
            return "Please specify which phone to delete."

    if record.find_phone(phone_to_remove):
        record.remove_phone(phone_to_remove)
        return "Phone deleted."

    return "Nothing to delete."
