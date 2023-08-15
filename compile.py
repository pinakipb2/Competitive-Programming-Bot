import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class CPPFileChangeHandler(FileSystemEventHandler):
    def __init__(self, cpp_filename):
        super().__init__()
        self.cpp_filename = cpp_filename

    def on_modified(self, event):
        if event.src_path.endswith(self.cpp_filename):
            print(f"Changes detected in {self.cpp_filename}. Recompiling ...")
            self.compile_cpp()


    def compile_cpp(self):
        compile_cmd = ["g++", self.cpp_filename, "-o", self.cpp_filename.replace(".cpp", "")]
        try:
            subprocess.run(compile_cmd, check=True)
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"[{Fore.CYAN + timestamp + Style.RESET_ALL}] - {Fore.GREEN}{self.cpp_filename} compiled successfully.{Style.RESET_ALL}")
            return self.cpp_filename.replace(".cpp", "")
        except subprocess.CalledProcessError:
            timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"[{Fore.CYAN + timestamp + Style.RESET_ALL}] - {Fore.RED}{self.cpp_filename} compilation failed.{Style.RESET_ALL}")
            return None

if __name__ == "__main__":
    folder_path = input(f"{Fore.CYAN}Enter the folder path containing CPP files: {Style.RESET_ALL}")

    if not os.path.isdir(folder_path):
        print(f"{Fore.RED}Invalid folder path.{Style.RESET_ALL}")
    else:
        os.chdir(folder_path)
        current_dir = os.getcwd()
        print(f"{Fore.GREEN}Currently watching : {current_dir}{Style.RESET_ALL}")
        for letter in range(ord('a'), ord('h') + 1):
            cpp_filename = chr(letter) + ".cpp"
            if os.path.isfile(cpp_filename):
                handler = CPPFileChangeHandler(cpp_filename)
                observer = Observer()
                observer.schedule(handler, path=current_dir, recursive=False)
                observer.start()

        print(f"{Fore.YELLOW}Watching for changes in CPP files. Press Ctrl+C to exit.{Style.RESET_ALL}")
        try:
            while True:
                pass
        except KeyboardInterrupt:
            observer.stop()

        observer.join()
