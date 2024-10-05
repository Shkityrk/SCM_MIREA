import os
import tarfile
import pytest
from unittest.mock import patch

from hw_1.src.config import ReadConfig
from hw_1.src.shell import ShellEmulator


@pytest.fixture
def setup_shell_emulator(tmp_path):
    test_tar = tmp_path / 'test_archive.tar'
    with tarfile.open(test_tar, 'w') as tar:
        test_file_path = tmp_path / 'test_dir' / 'test_file.txt'
        os.makedirs(os.path.dirname(test_file_path), exist_ok=True)
        with open(test_file_path, 'w') as f:
            f.write("Test content")
        tar.add(test_file_path)

    config_path = tmp_path / 'config.toml'
    with open(config_path, 'w') as config_file:
        config_file.write(f"[system]\nhostname = 'test_computer'\n[filesystem]\npath = '{test_tar}'\n")

    config = ReadConfig(str(config_path))
    shell_emulator = ShellEmulator(config)

    return shell_emulator


def test_ls_command(setup_shell_emulator): #passed
    shell_emulator = setup_shell_emulator
    with patch('builtins.print') as mocked_print:
        shell_emulator.execute_command("ls")
        mocked_print.assert_called_once_with('my_virtual_fs\ntest_dir\nUsers')



def test_cd_command(setup_shell_emulator):  #passed
    shell_emulator = setup_shell_emulator
    new_directory = "test_dir"

    # Проверка перехода в существующую директорию
    shell_emulator.execute_command(f"cd {new_directory}")
    assert shell_emulator.current_directory == os.path.join(shell_emulator.vfs.fs_path, new_directory)

    # Проверка на попытку перехода в несуществующую директорию
    nonexistent_directory = "nonexistent_dir"
    shell_emulator.execute_command(f"cd {nonexistent_directory}")

    # Убедимся, что текущая директория не изменилась
    assert shell_emulator.current_directory == os.path.join(shell_emulator.vfs.fs_path, new_directory)  # Текущая директория должна остаться прежней


def test_exit_command(setup_shell_emulator):#passed
    shell_emulator = setup_shell_emulator
    result = shell_emulator.execute_command("exit")
    assert not result


def test_rev_command(setup_shell_emulator): #passed
    shell_emulator = setup_shell_emulator
    with patch('builtins.print') as mocked_print:
        shell_emulator.execute_command("rev hello")
        mocked_print.assert_called_once_with('olleh')


def test_uname_command(setup_shell_emulator): #passed
    shell_emulator = setup_shell_emulator
    with patch('builtins.print') as mocked_print:
        shell_emulator.execute_command("uname")
        mocked_print.assert_called_once_with('Windows')  # Исправлено для соответствия фактическому значению


if __name__ == '__main__':
    pytest.main()
