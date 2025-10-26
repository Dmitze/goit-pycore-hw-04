def parse_input(user_input):
    parts = user_input.split()
    cmd, *args = parts
    return cmd.strip().lower(), args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Контакт додано."
    except ValueError:
        return "Помилка: для додавання контакту введіть ім'я та номер телефону."


def change_contact(args, contacts):
    try:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Контакт оновлено."
        else:
            return "Помилка: контакт не знайдено."
    except ValueError:
        return "Помилка: для зміни контакту введіть ім'я та новий номер."


def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Контакт не знайдено."
    except IndexError:
        return "Помилка: введіть ім'я контакту."


def show_all(contacts):
    if not contacts:
        return "Список контактів порожній."
    # Форматуємо вивід для кращої читабельності
    result = "Збережені контакти:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    contacts = {}
    print("Ласкаво просимо до бота-помічника!")

    while True:
        user_input = input("Введіть команду: ").strip()
        if not user_input:
            continue
        
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("До побачення!")
            break
        elif command == "hello":
            print("Чим я можу допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Невірна команда.")


if __name__ == "__main__":
    main()
