from datetime import datetime, date
from src.entities import Field
from src import CustomValueError


class Birthday(Field):
    """
    Class for field with birth date of contact
    """

    def validate_value(self, value: str) -> datetime:
        """
        For this field value should be valid date in format DD.MM.YYYY
        """
        birthdate = None
        try:
            birthdate = datetime.strptime(value, "%d.%m.%Y").date()
            if birthdate > datetime.now().date():
                raise CustomValueError(f"Birth date from future: {value}")
        except CustomValueError as e:
            raise e
        except ValueError as e:
            raise CustomValueError(
                "Invalid date format. Use DD.MM.YYYY"
            ) from e
        return birthdate

    def __str__(self):
        if self._value:
            return self._value.strftime("%d.%m.%Y")
        return ""
    
    def get_birthday_as_date(self):
        """
        This method returns birthday as datetime date
        """
        return self._value

    def days_to_next_birthday(self) -> int | None:
        """
        Returns the number of days until the next birthday.
        If birthday value is not set, returns None.
        """
        birthdate = self.get_birthday_as_date()
        if not birthdate:
            return None

        today = date.today()
        year = today.year

        # Try to set next birthday in the current year
        try:
            next_birthday = birthdate.replace(year=year)
        except ValueError:
            # This usually happens for Feb 29 on non-leap year
            # In that case, consider Feb 28 as the placeholder for calculation
            # (adjust as per your business rules if needed)
            next_birthday = birthdate.replace(year=year, month=2, day=28)

        # If birthday this year already passed, move to next year
        if next_birthday < today:
            try:
                next_birthday = birthdate.replace(year=year + 1)
            except ValueError:
                next_birthday = birthdate.replace(
                    year=year + 1,
                    month=2,
                    day=28,
                )

        days_left = (next_birthday - today).days
        return days_left
