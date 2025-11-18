"""
Entry point
"""

import pickle
import shlex
from collections import defaultdict
from colorama import Fore, Style, init
from src.handlers import *
from src.entities import AddressBook
from src.entities import NoteBook

def save_data(book: list, filename: str="books.pkl") -> None:
    """
    Save AddressBook and NoteBook to a binary file with the full object hierarchy.
    "filename" may be empty or None to indicate that no saving is necessary.
    """
    if not filename:
        return
    try:
        with open(filename, "wb") as file:
            pickle.dump(book, file)
    except IOError as e:
        print(f"Error saving state: {e}")

def load_data(filename: str="books.pkl") -> AddressBook:
    """
    Load AddressBook previously saved by "save_data" function
    """
    # empty str or None indicate to start with empty AddressBook
    if not filename:
        return AddressBook(), NoteBook()
    try:
        with open(filename, "rb") as file:
            books = pickle.load(file)
            return books[0], books[1]
    except (IOError, EOFError) as e:
        # EOFError is for wrong file format
        print(f"Warning: unable to load state from '{filename}': {e}")
        return AddressBook(), NoteBook()


def main(start_empty: bool = False, filename: str = "books.pkl"):
    """
    Main loop for bot

    "start_empty" flag indicates to start with empty AddressBook
        and to use filename to save final state only.
    
    "filename" is a path to file to save database state. 
        None or empty string would indicate to work in memory only. 
    """

    init(autoreset=True)

    if start_empty:
        contacts, notes = load_data(None)
    else:
        contacts, notes = load_data(filename)

    # command handlers

    def default_handler():
        def inner(*args, **kwargs):
            return "Invalid command."
        return inner

    # all handlers should take 2 arguments - args list and contacts dictionary
    handlers = defaultdict(default_handler, {
        "hello": lambda x, y, z: "How can I help you?",
        "close": lambda x, y, z: "Good bye!",
        "exit": lambda x, y, z: "Good bye!",
        "add": add_contact,
        "add-phone": add_contact,
        "change": change_contact,
        "change-phone": change_contact,
        "change-email": change_email,
        "delete": delete_contact,
        "delete-phone": delete_phone,
        "delete-email": delete_email,
        "delete-address": delete_address,
        "phone": show_phone,
        "show-phone": show_phone,
        "all": show_all,
        "add-birthday": add_birthday,
        "add-email": add_email,
        "add-address": add_address,
        "change-address": add_address,
        "show-birthday": show_birthday,
        "show-email": show_email,
        "show-address": show_address,
        "show-contact": show_contact,
        "birthdays": birthdays,
        "?": show_help,
        "help": show_help,
        "add-note": add_note,
        "show-notes": show_all_notes,
        "add-note-tag": add_note_tag,
        "remove-note-tag": remove_note_tag,
        "delete-note-tag": remove_note_tag,
        "remove-note": delete_note,
        "delete-note": delete_note,
        "notes-by-tag": show_notes_by_tag,
        "search-contacts": search_contacts,
        "search-notes": search_notes,
        "search": search_books,
    })

    print(show_help(None, None, None))

    # main loop
    command = ""
    prompt_text = f"{Fore.MAGENTA}Enter a command:{Style.RESET_ALL} "
    while command not in ["close", "exit"]:
        quotes_ok = False
        full_user_input = []
        one_cycle_prompt = prompt_text
        empty_lines_counter = 3
        while not quotes_ok and empty_lines_counter > 0:
            user_input = input(one_cycle_prompt)
            if user_input:
                empty_lines_counter = 3
            else:
                empty_lines_counter -= 1
            one_cycle_prompt = " "*16
            full_user_input.append(user_input)
            try:
                shlex.split("\n".join(full_user_input))
                quotes_ok = True
            except ValueError as e:
                if str(e) != "No closing quotation":
                    print("Wrong command format")

        command, *args = parse_input("\n".join(full_user_input))
        print(handlers[command](args, contacts, notes))

    save_data([contacts, notes], filename)


if __name__ == "__main__":
    main()
