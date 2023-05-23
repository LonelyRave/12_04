class Contact:
    def __init__(self, first_name, last_name='', phone_number='', birth_date=''):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._birth_date = birth_date

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def birth_date(self):
        return self._birth_date


class PhoneBook:
    def __init__(self):
        self._contacts = []
        self._emergency_numbers = {
            'Police': '102',
            'Fire Department': '101',
            'Ambulance': '103'
        }

    def add_contact(self, contact):
        self._contacts.append(contact)

    def remove_contact(self, contact):
        if contact in self._contacts:
            self._contacts.remove(contact)

    def edit_contact(self, contact, new_phone_number, new_birth_date):
        if contact in self._contacts:
            contact._phone_number = new_phone_number
            contact._birth_date = new_birth_date

    def list_contacts(self):
        return self._contacts

    def list_emergency_numbers(self):
        return self._emergency_numbers


class Interface:
    def __init__(self, phone_book):
        self._phone_book = phone_book

    def start(self):
        print('Welcome to the Phone Book App!')
        while True:
            print('\nSelect an option:')
            print('1. List contacts')
            print('2. Add contact')
            print('3. Remove contact')
            print('4. Edit contact')
            print('5. List emergency numbers')
            print('6. Exit')

            choice = input('Enter your choice: ')

            if choice == '1':
                self.list_contacts()
            elif choice == '2':
                self.add_contact()
            elif choice == '3':
                self.remove_contact()
            elif choice == '4':
                self.edit_contact()
            elif choice == '5':
                self.list_emergency_numbers()
            elif choice == '6':
                print('Exiting the Phone Book App...')
                break
            else:
                print('Invalid choice. Please try again.')

    def list_contacts(self):
        contacts = self._phone_book.list_contacts()
        if contacts:
            print('Contacts:')
            for contact in contacts:
                print(f'{contact.first_name} {contact.last_name} - {contact.phone_number}')
        else:
            print('No contacts found.')

    def add_contact(self):
        print('Enter contact details:')
        first_name = input('First name: ')
        last_name = input('Last name (optional): ')
        phone_number = input('Phone number: ')
        birth_date = input('Birth date (optional): ')

        contact = Contact(first_name, last_name, phone_number, birth_date)
        self._phone_book.add_contact(contact)
        print('Contact added successfully.')

    def remove_contact(self):
        self.list_contacts()
        contacts = self._phone_book.list_contacts()
        if contacts:
            index = input('Enter the index of the contact to remove: ')
            if index.isdigit() and int(index) < len(contacts):
                contact = contacts[int(index)]
                if contact.first_name not in self._phone_book.list_emergency_numbers().values():
                    self._phone_book.remove_contact(contact)
                    print('Contact removed successfully.')

    def list_emergency_numbers(self):
        emergency_numbers = self._phone_book.list_emergency_numbers()
        if emergency_numbers:
            print('Emergency Numbers:')
            for name, number in emergency_numbers.items():
                print(f'{name}: {number}')
        else:
            print('No emergency numbers found.')
