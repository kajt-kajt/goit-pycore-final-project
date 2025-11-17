from colorama import Fore, Style

HELP_PADDING = 32
TITLE_COLOR = Fore.LIGHTGREEN_EX
SECTION_COLOR = Fore.MAGENTA
COMMAND_COLOR = Fore.CYAN
DESCRIPTION_COLOR = Fore.LIGHTWHITE_EX


def _format_entry(command: str, description: str) -> str:
    padded = command.ljust(HELP_PADDING)
    return (
        f"{COMMAND_COLOR}{padded}{Style.RESET_ALL}"
        f" - {DESCRIPTION_COLOR}{description}{Style.RESET_ALL}"
    )


def show_help(_: list[str], __, ___) -> str:
    """
    Display formatted help text with grouped commands.
    """
    sections = [
        (
            "Available commands:",
            [
                ("hello", "Greet the assistant."),
                ("birthdays [days]", "Show upcoming birthdays (default: 7 days)."),
            ],
        ),
        (
            "--- Contact Management ---",
            [
                ("all", "Show all contacts."),
                ("add/add-phone <name> <phone>", "Add a new contact or phone."),
                ("change/change-phone <name> <old> <new>", "Update an existing phone."),
                ("delete <name>", "Delete an entire contact."),
                ("delete-phone <name> [phone]", "Remove a phone (if only one, argument optional)."),
                ("phone/show-phone <name>", "Show phone numbers for a contact."),
                ("add-birthday <name> <dd.mm.yyyy>", "Save a birthday for a contact."),
                ("show-birthday <name>", "Show a saved birthday."),
                ("add-email <name> <email>", "Link email to a name."),
                ("change-email <name> <old> <new>", "Replace a saved email."),
                ("delete-email <name> [email]", "Remove an email (if only one, argument optional)."),
                ("show-email <email>", "Find person using email."),
                ("add-address/change-address <name> <address>", "Add address."),
                ("change-address <name> <address>", "Update address."),
                ("delete-address <name>", "Remove saved address."),
                ("show-address <name>", "Display address for a contact."),
                ("show-contact <name>", "Show full record for a contact."),
            ],
        ),
        (
            "--- Note Management ---",
            [
                ("add-note <text>", "Add a new note and assign it an ID."),
                ("show-notes", "Display all stored notes."),
                ("add-note-tag <id> <tag>", "Attach one or more tags to a note."),
                ("remove-note-tag <id> <tag>", "Remove tags from a note."),
                ("delete-note <id>", "Delete a note by its ID."),
                ("notes-by-tag <tag>", "Show all notes containing the given tag."),
            ],
        ),
        (
            "--- Other Commands ---",
            [
                ("help, ?", "Print all commands."),
                ("close, exit", "Exit the assistant."),
            ],
        ),
    ]

    lines: list[str] = [f"{TITLE_COLOR}Welcome to the assistant bot!{Style.RESET_ALL}", ""]
    for section_title, entries in sections:
        lines.append(f"{SECTION_COLOR}{section_title}{Style.RESET_ALL}")
        for command, description in entries:
            lines.append(_format_entry(command, description))
        lines.append("")
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


if __name__ == "__main__":

    print(show_help([], None, None))
