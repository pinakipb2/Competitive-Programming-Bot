import os
import shutil
import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def create_folder_structure(folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        response = input(f"{Fore.YELLOW}The folder '{folder_name}' already exists.\nDo you want to override it? (y/n): {Style.RESET_ALL}")
        if response.lower() == 'n':
            print(f"{Fore.RED}Aborted.{Style.RESET_ALL}")
            return
        elif response.lower() != 'y':
            print(f"{Fore.RED}Invalid response. Aborted.{Style.RESET_ALL}")
            return
        shutil.rmtree(folder_name)
        os.mkdir(folder_name)

    os.chdir(folder_name)
    os.system("code .")

    for letter in range(ord('a'), ord('h') + 1):
        cpp_file_name = chr(letter) + ".cpp"
        with open(cpp_file_name, 'w') as cpp_file:
            pass  # Create an empty .cpp file
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"[{Fore.CYAN + timestamp + Style.RESET_ALL}] -{Fore.GREEN} Folder structure created successfully.{Style.RESET_ALL}")

if __name__ == "__main__":
    user_input_folder = input(f"{Fore.CYAN}Enter folder name: {Style.RESET_ALL}")
    create_folder_structure(user_input_folder)
