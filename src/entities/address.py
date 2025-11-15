from src.entities import Field
from src import CustomValueError

class Address(Field):
    """
    Class for address entity. Value must be at least 5 symbols long.
    """

    def validate_value(self, value: str) -> str:
        """
        Address must be at least 5 symbols long
        """
        value_str = super().validate_value(value)
        if not len(value_str)>4:
            error_msg = f"Address must be at least 5 symbols long, got '{value_str}' instead."
            raise CustomValueError(error_msg)
        return value_str