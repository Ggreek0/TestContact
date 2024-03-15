# # Простий застосунок для керування списком контактів

import unittest


class Contact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def search_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None


class TestContact(unittest.TestCase):
    def test_contact_creation(self):
        contact = Contact("Микола", "Шевченко", "0992756068", "mykolashef@gmail.com")
        self.assertEqual(contact.first_name, "Микола")
        self.assertEqual(contact.last_name, "Шевченко")
        self.assertEqual(contact.phone_number, "0992756068")
        self.assertEqual(contact.email, "mykolashef@gmail.com")


class TestAddressBook(unittest.TestCase):
    def setUp(self):
        self.address_book = AddressBook()
        self.contact1 = Contact("Микола", "Шевченко", "0992756068", "mykolashef@gmail.com")
        self.contact2 = Contact("Євгеній", "Коваль", "0663940527", "evgenkoval@gmail.com")
        self.address_book.add_contact(self.contact1)
        self.address_book.add_contact(self.contact2)

    def test_add_contact(self):
        self.assertEqual(len(self.address_book.contacts), 2)

    def test_remove_contact(self):
        self.address_book.remove_contact(self.contact1)
        self.assertEqual(len(self.address_book.contacts), 1)

    def test_search_contact(self):
        found_contact = self.address_book.search_contact("Микола", "Шевченко")
        self.assertEqual(found_contact, self.contact1)


if __name__ == '__main__':
    unittest.main()
