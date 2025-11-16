# shell-like argument parsing
import shlex
from typing import Callable
from dataclasses import dataclass
from src.handlers.input_error import input_error
#from src.ui.command_list import COMMANDS

@dataclass
class CommandHandler():
    """
    Represents command handler - function to call plus some additional parameters
    """
    handler_function: Callable
    description: str

@input_error
def parse_input(user_input: str, command_tree: dict) -> tuple[Callable,list[str]]:
    """
    Parses user input into command and arguments.
    """
    args = shlex.split(user_input.strip())
    return get_handler(args, command_tree)
    #cmd = cmd.strip().lower()
    #return cmd, *args

def get_handler(args: list[str], command_tree: dict) -> tuple[Callable,list[str]]:
    params = []
    named_param = None
    named_param_subtree = None
    for word, subtree in command_tree.items():
        # checking all fixed-value words first
        if word.startswith("<") and word.endswith(">"):
            named_param = word[1:-1]
            named_param_subtree = subtree
        elif args[0].casefold() == word.casefold():
            if len(args)==1:
                if isinstance(subtree, CommandHandler):
                    return subtree, params
            else:
                handler, params = get_handler(args[1:],subtree)
                if handler:
                    return handler, params
        # if Handler is still not found:
    if named_param:
        handler, params = get_handler(args[1:],named_param_subtree)
        if handler:
            params.insert(0, args[0])
            return handler, params
    raise ValueError("Cannot recognize command. See help for full list.")

