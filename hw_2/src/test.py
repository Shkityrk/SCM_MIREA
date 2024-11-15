import unittest
from utils import parse_dependencies, generate_plantuml_script

class TestUtils(unittest.TestCase):
    def test_parse_dependencies(self):
        deps = parse_dependencies("test_package", 2)
        self.assertIsInstance(deps, dict)

    def test_generate_plantuml_script(self):
        deps = {"root": ["child1", "child2"]}
        script = generate_plantuml_script(deps)
        self.assertIn("@startuml", script)
        self.assertIn("@enduml", script)
        self.assertIn('"root" --> "child1"', script)

if __name__ == "__main__":
    unittest.main()
