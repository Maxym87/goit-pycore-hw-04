def user_input(commands):
    cmd, *args = commands.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contacts(args, contacts):
    if len(args) != 2:
        return 'Помилка вводу! Введіть, будь ласка, і\'мя та номер телефону'
    name, phone = args
    contacts[name] = phone
    return 'Контакт додано'

def change_contacts(args, contacts):
    if len(args) != 2:
        return 'Помилка вводу! Введіть, будь ласка, і\'мя та номер телефону'
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return 'Контакт оновлено'
    else:
        return 'Контакт не знайдений'
    
def show_phone(args, contacts):
    if len(args) != 1:
        return 'Помилка вводу! Введіть, будь ласка, і\'мя'
    
    name = args[0]
    
    if name in contacts:
        return f'Контактний номер {name} - {contacts[name]}'
    else:
        return 'Контакт не знайдений'

def show_all(contacts):
    if not contacts:
        return 'Контакти відсутні'
    result = ''
    for name, phone in contacts.items():
        result += f'{name}: {phone}\n'
    return result.strip()

def main():
    contacts = {}
    print('Вас вітає бот-ассистент')

    while True:
        user_input_str = input('Введіть, будь ласка, команду: ')
        command, *args = user_input(user_input_str)
        
        if command in ['закрити', 'вийти']:
            print('До побачення')
            break
        elif command == 'вітаю':
            print('Чим я можу допомогти?')
        elif command == 'додати':
            print(add_contacts(args, contacts))
        elif command == 'змінити':
            print(change_contacts(args, contacts))
        elif command == 'показати контакт':
            print(show_phone(args, contacts))
        elif command == 'показати все':
            print(show_all(contacts))
        else:
            print('Невідома команда')

if __name__ == '__main__':
    main()
