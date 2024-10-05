import subprocess
import os

__all__=[
    "PlantUMLRenderer",
]

class PlantUMLRenderer:
    def __init__(self, plantuml_path):
        self.plantuml_path = plantuml_path

    def render(self, uml_content, output_path):
        uml_file = 'graph.puml'
        with open(uml_file, 'w') as file:
            file.write(uml_content)

        try:
            result = subprocess.run(['java', '-jar', self.plantuml_path, '-tsvg', uml_file], check=True)
            print("PlantUML успешно выполнен.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении PlantUML: {e}")
            return

        svg_file = 'graph.svg'
        if os.path.exists(svg_file):
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            os.rename(svg_file, output_path)
        else:
            print("Файл 'graph.svg' не найден.")
