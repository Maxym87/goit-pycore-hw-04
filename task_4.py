
def user_input(message):
    cmd, *args = message.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contacts(args, contacts):
    if len(args) !=2:
        return 'Помилка вводу! Введіть, будь ласка, і\'мя та номер телефону'
    neme, phone = args
    contacts[name] = phone
    return 'Додайте контакти'

def change_contacts(args, contacts):
    if len(args) !=2:
        return 'Помилка вводу! Введіть, будь ласка, і\'мя та номер телефону'
    if name in contacts:
        contacts[name] = phone
        return 'Контакт оновлено'
    else:
        return 'Помилка оновлення контакту'
    
def show_phone(args, contacts):
    if len(args) !=2:
        return 'Помилка вводу! Введіть, будь ласка, і\'мя'
    
    name = args[0]
    
    if name in contacts:
        return f'Контактний номер {name} - {contacts[name]}'