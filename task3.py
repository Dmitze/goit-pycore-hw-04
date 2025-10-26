import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init(autoreset=True)

def display_directory_structure(directory_path, indent=""):
    path = Path(directory_path)
    if not path.exists():
        print(Fore.RED + f"Помилка: Шлях '{directory_path}' не існує.")
        return
    if not path.is_dir():
        print(Fore.RED + f"Помилка: '{directory_path}' не є директорією.")
        return

    # Виводимо назву поточної директорії
    print(indent + Fore.BLUE + f" {path.name}/")

    for item in sorted(path.iterdir()):
        if item.is_dir():
            # Рекурсивний виклик для піддиректорій
            display_directory_structure(item, indent + "    ")
        else:
            print(indent + "    " + Fore.GREEN + f" {item.name}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
        display_directory_structure(target_path)
    else:
        print(Fore.YELLOW + "Будь ласка, вкажіть шлях до директорії як аргумент командного рядка.")
