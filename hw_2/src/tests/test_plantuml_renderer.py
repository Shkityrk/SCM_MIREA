# src/tests/test_plantuml_renderer.py

import unittest
from unittest.mock import patch

from hw_2.src.config import PLANTUML_PATH
from hw_2.src.graph import PlantUMLRenderer


class TestPlantUMLRenderer(unittest.TestCase):

    @patch('subprocess.run')
    def test_render_success(self, mock_run):

        renderer = PlantUMLRenderer(PLANTUML_PATH)

        # Здесь предполагается, что граф сохраняется в файл 'graph.puml'
        renderer.render('graph.puml', 'output/graph.svg')

        # Проверка, что subprocess.run был вызван с правильными аргументами
        mock_run.assert_called_once_with(
            ['java', '-jar', PLANTUML_PATH, '-tsvg', 'graph.puml'],
            check=True
        )

    @patch('subprocess.run')
    def test_render_failure(self, mock_run):
        mock_run.side_effect = Exception("Error during rendering")

        renderer = PlantUMLRenderer(PLANTUML_PATH)

        with self.assertRaises(Exception) as context:
            renderer.render('graph.puml', 'output/graph.svg')

        self.assertEqual(str(context.exception), "Error during rendering")

if __name__ == '__main__':
    unittest.main()
