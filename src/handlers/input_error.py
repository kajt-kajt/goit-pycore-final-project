from functools import wraps
from typing import Callable
from src import CustomValueError


def input_error(func: Callable) -> Callable:
    """
    Decorator to handle typical errors caused by wrong user input.
    Adds help hint to all general error messages.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except CustomValueError as e:
            return f"{e}. Type 'help' to see available commands."

        except (ValueError, IndexError):
            return "Wrong argument(-s) provided. Type 'help' to see available commands."

        except KeyError:
            return "No such contact found. Type 'help' to see available commands."

    return inner
