import platform



__all__=[
    "ShellEmulator"
]

from hw_1.src.config import VirtualFileSystem


class ShellEmulator:
    def __init__(self, config):
        self.computer_name = config.get_computer_name()
        self.vfs = VirtualFileSystem(config.get_filesystem_path())
        self.current_directory = self.vfs.fs_path

    def shell_prompt(self):
        return f"{self.computer_name}:{self.current_directory}$ "

    def execute_command(self, command):
        if command == "exit":
            return False
        elif command == "ls":
            print("\n".join(self.vfs.list_directory(self.current_directory)))
        elif command.startswith("cd "):
            new_directory = command.split(" ", 1)[1]
            try:
                self.current_directory = self.vfs.change_directory(self.current_directory, new_directory)
            except FileNotFoundError as e:
                print(e)
        elif command.startswith("rev "):
            string_to_reverse = command.split(" ", 1)[1]
            print(string_to_reverse[::-1])  # Вывод строки в обратном порядке
        elif command == "uname":
            print(platform.system())  # Вывод имени операционной системы
        else:
            print(f"Command '{command}' not found.")
        return True

    def run(self):
        while True:
            command = input(self.shell_prompt())
            if not self.execute_command(command):
                break