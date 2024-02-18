class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        contact = Contact(name, phone_number, email)
        self.contacts.append(contact)
        print("\nContact added successfully.")

    def view_all_contacts(self):
        if self.contacts:
            print("\nAll Contacts:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"\nContact {index}:\n{contact}")
        else:
            print("\nAddress book is empty.")

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name.lower()]
        if found_contacts:
            print("\nMatching Contacts:")
            for index, contact in enumerate(found_contacts, start=1):
                print(f"\nContact {index}:\n{contact}")
        else:
            print("\nNo matching contacts found.")

    def update_contact(self, name, new_phone_number, new_email):
        found = False
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.phone_number = new_phone_number
                contact.email = new_email
                found = True
                break
        if found:
            print("\nContact updated successfully.")
        else:
            print("\nContact not found.")

    def delete_contact(self, name):
        found = False
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                found = True
                break
        if found:
            print("\nContact deleted successfully.")
        else:
            print("\nContact not found.")


def main():
    address_book = AddressBook()

    while True:
        print("\nAddress Book Menu:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            print("\nAdd Contact:")
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address_book.add_contact(name, phone_number, email)
        elif choice == "2":
            address_book.view_all_contacts()
        elif choice == "3":
            print("\nSearch Contact:")
            name = input("Enter name to search: ")
            address_book.search_contact(name)
        elif choice == "4":
            print("\nUpdate Contact:")
            name = input("Enter name of contact to update: ")
            new_phone_number = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            address_book.update_contact(name, new_phone_number, new_email)
        elif choice == "5":
            print("\nDelete Contact:")
            name = input("Enter name of contact to delete: ")
            address_book.delete_contact(name)
        elif choice == "6":
            print("\nExiting Address Book. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please choose again.")


if __name__ == "__main__":
    main()
