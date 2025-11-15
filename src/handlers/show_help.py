HELP_PADDING = 32


def _format_entry(command: str, description: str) -> str:
    return f"{command.ljust(HELP_PADDING)} - {description}"


def show_help(_: list[str], __) -> str:
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
                ("add <name> <phone>", "Add a new contact or phone."),
                ("change <name> <old> <new>", "Update an existing phone."),
                ("phone <name>", "Show phone numbers for a contact."),
                ("add-birthday <name> <dd.mm.yyyy>", "Save a birthday for a contact."),
                ("show-birthday <name>", "Show a saved birthday."),
                ("add-email <name> <email>", "Link email to a name."),
                ("show-email <email>", "Find person using email."),
            ],
        ),
        (
            "--- Other Commands ---",
            [
                ("help", "Print all commands."),
                ("close, exit", "Exit the assistant."),
            ],
        ),
    ]

    lines: list[str] = ["Welcome to the assistant bot!"]
    for section_title, entries in sections:
        lines.append(section_title)
        for command, description in entries:
            lines.append(_format_entry(command, description))
        lines.append("")
    return "\n".join(lines).rstrip()


if __name__ == "__main__":
    print(show_help([], None))
