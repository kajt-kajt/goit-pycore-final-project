from src.handlers.input_error import input_error
from src.entities import AddressBook

@input_error
def birthdays(args: list[str], book: AddressBook, __):
    """
    Display list of contacts for greeting for the period of time specified.
    By default period is 7 days, but may be provided as argument.
    """
    days = 7
    try:
        days = int(args[0])
    except (ValueError, IndexError):
        pass

    users_with_birthdays = [record for record in book.values() if record.birthday]
    upcoming_birthdays = [record for record in users_with_birthdays 
                          if record.birthday.days_to_next_birthday() <= days]
    upcoming_birthdays.sort(key = lambda x: x.birthday.days_to_next_birthday())
    result = "\n".join([str(record) for record in upcoming_birthdays])
    return result

