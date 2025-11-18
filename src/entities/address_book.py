from collections import UserDict
from src.entities import Record


class AddressBook(UserDict):
    """
    Class for address book entity, extends dict, so has its main object in the
    data field. Key for the dictionary would be name as str for easier search.
    """

    def __setitem__(self, key, item):
        """
        If item to add is not of class Record - let's convert it to Record
        """
        if isinstance(item, Record):
            # value is Record, some internal call
            return super().__setitem__(key, item)
        else:
            # new name
            value = Record(key)
            value.add_phone(item)
            return super().__setitem__(key, value)

    def add_record(self, record: Record):
        """
        Add record to address book. If such name already exists, record will be
        rewritten.
        """
        if not isinstance(record, Record):
            error_msg = (
                "Expecting object of type Record, but got "
                f"{type(record).__name__} instead."
            )
            raise ValueError(error_msg)
        self[str(record.name)] = record

    def find(self, name: str) -> Record:
        """
        Get record by name. Return None if record with such name does not exist.
        """
        return self.get(name)

    def delete(self, name: str) -> Record:
        """
        Delete record from address book by name and return it back.
        Return None if record was not found.
        """
        return self.pop(name, None)

    def search_by_pattern(self, pattern: str) -> str:
        """
        Search all text fields of each record for a match of a pattern
        """
        results = [record.search_by_pattern(pattern) for record in self.values()]
        return "\n".join([value for value in results if value])

