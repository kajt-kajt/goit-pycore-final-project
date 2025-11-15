import re

from src.entities import Field


class CustomValueException(ValueError):
    """
    Raised when email value does not match expected format.
    """


class Email(Field):
    """
    Class for email entity.
    """

    _email_regex = re.compile(
        r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$"
    )

    def validate_value(self, value: str) -> str:
        """
        Must match email format
        """
        value_str = super().validate_value(value).strip()

        if not value_str:
            raise CustomValueException("Email can not be empty.")

        if not self._email_regex.fullmatch(value_str):
            error_msg = f"Email format is not valid, got '{value_str}' instead."
            raise CustomValueException(error_msg)

        return value_str
    
