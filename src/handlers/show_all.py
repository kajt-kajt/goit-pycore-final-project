from colorama import Fore, Style
from src.entities import AddressBook
from src.handlers.input_error import input_error


def _format_record(record) -> str:
    birthday = record.get_birthday()
    phones = record.get_phones()
    address = record.get_address()
    emails = record.get_emails()

    def label(text: str) -> str:
        return f"{Fore.LIGHTGREEN_EX}{text}{Style.RESET_ALL}"

    lines = [
        f"{label('Name:')} {record.name}",
        f"{label('Birthday:')} {birthday if birthday else '-'}",
        f"{label('Phones:')} {phones + ';' if phones else '-'}",
        f"{label('Address:')} {address if address else '-'}",
        f"{label('Emails:')} {emails if emails else '-'}",
    ]
    return "\n".join(lines)


def show_all(_, contacts: AddressBook, __) -> str:
    """
    Outputs all the contents of in-memory database of contacts.
    """
    result = [_format_record(contacts[name]) for name in contacts]
    return "\n\n".join(result)


@input_error
def show_contact(args: list[str], contacts: AddressBook, _) -> str:
    """
    Outputs detailed information for a contact.
    """
    name = args[0]
    return _format_record(contacts[name])
