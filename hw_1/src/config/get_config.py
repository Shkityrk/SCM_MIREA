import os

import toml

__all__=[
    "ReadConfig",
]


class ReadConfig:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)

    def get_filesystem_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(current_dir, '..', 'env', 'filesystem.tar')

    def load_config(self, config_path):
        with open(config_path, 'r') as file:
            return toml.load(file)

    def get_computer_name(self):
        return self.config['system']['hostname']

    def get_filesystem_path(self):
        return self.config['filesystem']['path']

