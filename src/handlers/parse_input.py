import shlex
from src.handlers.input_error import input_error

@input_error
def parse_input(user_input: str) -> tuple[str,list[str]]:
    """
    Parses user input into command and arguments.
    """
    # shlex module takes care of arguments with parenthesis and escape sequences
    cmd, *args = shlex.split(user_input.strip())
    cmd = cmd.strip().lower()
    return cmd, *args
