from datetime import datetime
from src.entities import Name, Phone, Birthday, Email, Address


class Record:
    """
    Class representing a single record in address book with name and a list of
    phone numbers.
    """
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.address = None
        self.emails = []

    def __str__(self):
        birthday_info = self.get_birthday()
        if birthday_info:
            birthday_info = f"({birthday_info})"
        phones_info = '; '.join(str(p) for p in self.phones)
        emails_info = '; '.join(str(p) for p in self.emails)
        delimiter1 = ""
        delimiter2 = ""
        if phones_info and emails_info:
            delimiter2 = "; "
        if phones_info or emails_info:
            delimiter1 = ": "
        return (
            f"{self.name} {birthday_info}"
            f"{delimiter1}{phones_info}{delimiter2}{emails_info}"
        )

    def __repr__(self):
        return f"Record({str(self)})"

    def display_record(self) -> str:
        result = f"Name: {str(self.name)}"
        if self.birthday:
            birthday_info = datetime.strftime(self.birthday, "%d-%m-%Y")
            result = result + "\nBirthday: " + birthday_info
        if self.phones:
            phones = "; ".join([str(phone) for phone in self.phones])
            result = result + "\nPhones: " + phones
        if self.emails:
            emails = "; ".join([str(email) for email in self.emails])
            result = result + "\nEmails: " + emails
        if self.address:
            result = result + f"\nAddress: {self.address}"
        return result

    def add_phone(self, phone: str):
        """
        Add phone number to list for this record
        """
        if not self.find_phone(phone):
            self.phones.append(Phone(phone))

    def add_email(self, email: str):
        """
        Add email to list for this record
        """
        if not self.find_email(email):
            self.emails.append(Email(email))

    def remove_phone(self, phone: str):
        """
        Remove phone number from list for this record
        """
        self.phones = [phone_record for phone_record in self.phones if str(phone_record) != phone]

    def remove_email(self, email: str):
        """
        Remove email from list for this record
        """
        self.emails = [
            email_record
            for email_record in self.emails
            if str(email_record).casefold() != email.casefold()
        ]

    def edit_phone(self, old_phone: str, new_phone: str) -> bool:
        """
        Find phone number record in the list and update it with new value.
        Returns True if old number was found and replaced.
        Also function removes potential duplicates that might occur due to changes.
        """
        # also removing potential duplicates
        temp_list = []
        new_phones = []
        update_took_place = False
        for phone_record in self.phones:
            phone_record_str = str(phone_record)
            if str(phone_record) == old_phone:
                phone_record.update(new_phone)
                phone_record_str = str(phone_record)
                update_took_place = True
            if phone_record_str not in temp_list:
                temp_list.append(phone_record_str)
                new_phones.append(phone_record)
        self.phones = new_phones
        return update_took_place

    def edit_email(self, old_email: str, new_email: str) -> bool:
        """
        Find email record in the list and update it with new value.
        Returns True if old email was found and replaced.
        Also function removes potential duplicates that might occur due to changes.
        """
        # also removing potential duplicates
        temp_list = []
        new_emails = []
        update_took_place = False
        for email_record in self.emails:
            email_record_str = str(email_record)
            if str(email_record).casefold() == old_email.casefold():
                email_record.update(new_email)
                email_record_str = str(email_record)
                update_took_place = True
            if email_record_str not in temp_list:
                temp_list.append(email_record_str)
                new_emails.append(email_record)
        self.emails = new_emails
        return update_took_place

    def find_phone(self, phone: str) -> Phone | None:
        """
        Find phone number in the list
        """
        result = None
        for phone_record in self.phones:
            if str(phone_record) == phone:
                result = phone_record
                break
        return result

    def find_email(self, email: str) -> Email | None:
        """
        Find email in the list
        """
        result = None
        for email_record in self.emails:
            if str(email_record) == email:
                result = email_record
                break
        return result

    def get_phones(self) -> str:
        """
        Output all phone numbers in record
        """
        return '; '.join(str(p) for p in self.phones)

    def get_emails(self) -> str:
        """
        Output all emails in record
        """
        return '; '.join(str(p) for p in self.emails)

    def add_birthday(self, birthdate: str | None):
        """
        Add or update birthday field of the record
        """
        if birthdate is None:
            self.birthday = None
        else:
            self.birthday = Birthday(birthdate)
    
    def get_birthday(self) -> str:
        """
        Display birthday information for contact
        """
        if self.birthday is None:
            return ""
        return str(self.birthday)

    def add_address(self, address: str | None):
        """
        Add or update address field of the record
        """
        if address is None:
            self.address = None
        else:
            self.address = Address(address)
    
    def get_address(self) -> str:
        """
        Display address information for contact
        """
        if self.address is None:
            return ""
        return str(self.address)
    
    def search_by_pattern(self, pattern: str) -> str:
        """
        Search fields name, address, phones and emails by pattern
        """
        pattern_sanitized = pattern.strip().casefold()
        results = []
        # display_record
        if pattern_sanitized in str(self.name).casefold():
            results.append(f"Match by name: {str(self.name)}")
        if (
            self.address
            and pattern_sanitized in str(self.address).casefold()
        ):
            results.append(
                f"Match by address: {str(self.name)}: {str(self.address)}"
            )
        for phone in self.phones:
            if pattern_sanitized in str(phone).casefold():
                results.append(
                    f"Match by phone: {str(self.name)}: {str(phone)}"
                )
        for email in self.emails:
            if pattern_sanitized in str(email).casefold():
                results.append(
                    f"Match by email: {str(self.name)}: {str(email)}"
                )
        return "\n".join(results)
    
