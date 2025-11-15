from src.entities import Field
from src import CustomValueError

class Email(Field):
    """
    Class for email entity.
    """

    def validate_value(self, value: str) -> str:
        """
        Must match email format
        """
        value_str = super().validate_value(value)
        if value_str.count("@") != 1:
            error_msg = f"Email format is not valid, got '{value_str}' instead."
            raise CustomValueError(error_msg)
        return value_str
    