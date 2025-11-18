from src.handlers.input_error import input_error
from src.entities import AddressBook


@input_error
def delete_email(args: list[str], contacts: AddressBook, _) -> str:
    """
    Removes an email from the contact.
    If email is not provided and only one exists, it will be removed.
    """
    if not args:
        raise ValueError("No arguments provided.")

    name, *rest = args
    if name not in contacts:
        return f"ERROR: contact '{name}' does not exist!"

    record = contacts[name]
    email_to_remove = rest[0] if rest else None

    if email_to_remove is None:
        if len(record.emails) == 1:
            email_to_remove = str(record.emails[0])
        else:
            return "Please specify which email to delete."

    if record.find_email(email_to_remove):
        record.remove_email(email_to_remove)
        return "Email deleted."

    return "Nothing to delete."
