from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.valid_phone()
    def valid_phone(self):
        if len(self.value) != 10 or not self.value.isdigit():
            raise ValueError


class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phones = []

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        phone.valid_phone()
        self.phones.append(phone)

    def remove_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return

    def edit_phone(self, old_phone: str, new_phone: str):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError('Invalid phone number')

    def find_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name] = record

    def find(self, found_name: Name):
        for name, record in self.data.items():
            if name == found_name:
                return record

    def delete(self, deleted_name: Name):
        if deleted_name in self.data.keys():
            del self.data[deleted_name]


if __name__ == "__main__":
    book = AddressBook()


    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("555555555")


    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)


    for name, record in book.data.items():
        print(record)





