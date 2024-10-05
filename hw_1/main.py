from src.config import ReadConfig
from src.shell.emulator import ShellEmulator


import os


def main():
    config = ReadConfig(r"D:/Projects/SCM/hw_1/src/env/config.toml")
    # path = os.path.abspath(os.path.dirname(__file__)) + "/src/env/config.toml"

    shell = ShellEmulator(config)
    shell.run()


if __name__ == "__main__":
    main()
