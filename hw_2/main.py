from hw_2.src.config import PLANTUML_PATH, OUTPUT_PATH
from src.graph import DependencyGraph
from src.graph import PlantUMLRenderer


def main():
    dep_graph = DependencyGraph(max_depth=3)
    uml_content = dep_graph.generate_uml()

    # Генерация SVG
    renderer = PlantUMLRenderer(PLANTUML_PATH)
    renderer.render(uml_content, OUTPUT_PATH)

if __name__ == "__main__":
    main()
