import re

from src.entities import Field
from src import CustomValueError

class Phone(Field):
    """
    Class for phone number entity. Values are normalized to +380XXXXXXXXX format by default.
    """

    def validate_value(self, value: str) -> str:
        """
        Normalize phone numbers to international +380 format unless explicit country code is used.
        """
        value_str = super().validate_value(value)

        stripped_value = value_str.strip()
        if stripped_value.startswith("+"):
            cleaned = re.sub(r"[()\s]", "", stripped_value)
            digits_after_plus = re.sub(r"\D", "", cleaned[1:])
            if not digits_after_plus or len(digits_after_plus) < 7:
                raise CustomValueError("Phone number is too short.")
            return cleaned

        digits_only = re.sub(r"\D", "", value_str)

        if not digits_only:
            raise CustomValueError("Phone number must contain digits.")

        # Strip optional international prefix
        if digits_only.startswith("00"):
            digits_only = digits_only[2:]

        normalized_national = ""
        if digits_only.startswith("380") and len(digits_only) == 12:
            normalized_national = digits_only[3:]
        elif digits_only.startswith("0") and len(digits_only) == 10:
            normalized_national = digits_only[1:]
        elif len(digits_only) == 9:
            normalized_national = digits_only
        else:
            raise CustomValueError(
                f"Phone number '{value_str}' must represent a Ukrainian number."
            )

        if len(normalized_national) != 9:
            raise CustomValueError(
                f"Phone number '{value_str}' must have 9 digits after the code."
            )

        return f"+380{normalized_national}"


