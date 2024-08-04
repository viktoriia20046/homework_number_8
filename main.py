import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, phone, email):
        self.contacts[name] = {'phone': phone, 'email': email}

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
    
    def get_contact(self, name):
        return self.contacts.get(name, None)
    
    def list_contacts(self):
        return self.contacts
def save_data(book, filename="addressbook.pkl"):
    with open(filename, 'wb') as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data()
    
    print("Завантажено контакти:", book.list_contacts())  # Перевірка завантажених контактів

    while True:
        print("\nАдресна книга:")
        print("1. Додати контакт")
        print("2. Видалити контакт")
        print("3. Переглянути контакт")
        print("4. Переглянути всі контакти")
        print("5. Вийти")

        choice = input('Виберіть дію (1-5): ')
        if choice == '1':
            name = input("Введіть ім'я: ")
            phone = input("Введіть телефон: ")
            email = input("Введіть email: ")
            book.add_contact(name, phone, email)
        elif choice == '2':
            name = input("Введіть ім'я для видалення: ")
            book.remove_contact(name)
        elif choice == '3':
            name = input("Введіть ім'я для перегляду: ")
            contact = book.get_contact(name)
            if contact:
                print(f"Телефон: {contact['phone']}, Email: {contact['email']}")
            else:
                print("Контакт не знайдено.")
        elif choice == '4':
            contacts = book.list_contacts()
            if contacts:
                for name, info in contacts.items():
                    print(f"{name}: Телефон - {info['phone']}, Email - {info['email']}")
            else:
                print("Адресна книга порожня.")
        elif choice == '5':
            # Збереження даних перед виходом
            save_data(book)
            print("Дані збережено. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()