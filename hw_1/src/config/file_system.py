import os
import tarfile

__all__ = [
    "VirtualFileSystem",
]


class VirtualFileSystem:
    def __init__(self, tar_path, extract_path='/tmp/virtual_fs'):
        self.fs_path = self.load_virtual_fs(tar_path, extract_path)



    def load_virtual_fs(self, tar_path, extract_path):
        if not os.path.exists(extract_path):
            os.makedirs(extract_path)
        with tarfile.open(tar_path, 'r') as tar:
            tar.extractall(path=extract_path)
        return extract_path

    def list_directory(self, current_directory):
        return os.listdir(current_directory)

    def change_directory(self, current_directory, new_directory):
        new_path = os.path.join(current_directory, new_directory)
        if os.path.isdir(new_path):
            return new_path
        else:
            raise FileNotFoundError(f"Directory {new_directory} not found")