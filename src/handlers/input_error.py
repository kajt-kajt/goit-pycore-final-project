from functools import wraps
from typing import Callable
from src import CustomValueError


# handler decorator
def input_error(func: Callable) -> Callable:
    """
    Decorator to handle typical errors caused by wrong user input.
    """
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except CustomValueError as e:
            return str(e)
        except (ValueError, IndexError):
            return "Wrong argument(-s) provided. Type 'help' to see available commands."
        except KeyError:
            return "No such contact found. Type 'help' to see available commands."
    return inner
