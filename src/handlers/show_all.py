from src.entities import AddressBook
from src.handlers.input_error import input_error


def _format_record(_, record) -> str:
    birthday = record.get_birthday()
    phones = record.get_phones()
    address = record.get_address()
    emails = record.get_emails()

    lines = [
        f"Name: {record.name}",
        f"Birthday: {birthday if birthday else '- ;'}",
        f"Phones: {phones + ';' if phones else '- ;'}",
        f"Address: {address if address else '- ;'}",
        f"Emails: {emails if emails else '- ;'}",
    ]
    return "\n".join(lines)


def show_all(_, contacts: AddressBook) -> str:
    """
    Outputs all the contents of in-memory database of contacts.
    """
    result = [_format_record(name, contacts[name]) for name in contacts]
    return "\n\n".join(result)

@input_error
def show_contact(args: list[str], contacts: AddressBook) -> str:
    """
    Outputs all the contents of in-memory database of contacts.
    """
    name = args[0]
    result = f"{contacts[name]}"
    return result
