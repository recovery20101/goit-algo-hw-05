def input_error(func):
    """Декоратор для обробки помилок"""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Error: Invalid input. Please re-check arguments."
        except IndexError:
            return "Error: Missing required arguments."
        except KeyError:
            return "Error: Invalid name. Please check that name is correct."
    return inner

def parse_input(user_input):
    """Функція для парсінгу команд"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    args = [arg.lower() for arg in args]
    return cmd, *args

@input_error
def add_contact(args, contacts):
    """Функція для додавання контактів"""
    name, phone = args
    if name in contacts:
        return "Contact already exists."
    else:
        contacts[name] = phone
        return "Contact added."

@input_error
def change_contact(args, contacts):
    """Функція для зміни контактів"""
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact is missing."

@input_error    
def show_phone(args, contacts):
    """Функція для виводу телефону, прибрав get() щоб можна було перевірити KeyError"""
    name = args[0]
    phone = contacts[name]
    return phone
  
def all(contacts):
    """Функція для повернення списку контактів"""
    return contacts

def main():
    """Main функція""" 
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        """Виклик функцій в залежності від команди"""
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()