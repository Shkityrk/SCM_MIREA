__all__=[
    "DependencyGraph",
]

from hw_2.src.config import UML_FILE_PATH


class DependencyGraph:
    def __init__(self, max_depth):
        self.max_depth = max_depth

    def generate_uml(self):
        with open(UML_FILE_PATH, 'r') as file:
            uml_content = file.read()

        return uml_content

