import os
import sys
from colorama import init, Fore

init(autoreset=True)

def color_text(path):
    if not os.path.isdir(path):
        print(Fore.RED + f'Помилка! {path} не є директорією або вона не існує.')
        return
    
    for root, dirs, files in os.walk(path):
        print(Fore.CYAN + f'Директорія: {root}')

        for dir_name in dirs:
            print(Fore.BLUE + f'Папка: {dir_name}')

        for file_name in files:
            print(Fore.YELLOW + f'Файл: {file_name}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(Fore.RED + 'Будь ласка, вкажіть шлях до Директорії')
    else: path = sys.argv[1]