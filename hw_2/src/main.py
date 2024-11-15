import os
import csv
import subprocess
from utils import parse_dependencies, generate_plantuml_script, save_plantuml_script


def read_config(config_path):
    with open(config_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        config = {row['key']: row['value'] for row in reader}
    return config


def visualize_dependencies(config_path):
    config = read_config(config_path)
    program_path = config['program_path']
    package_path = config['package_path']
    output_path = config['output_path']
    max_depth = int(config['max_depth'])

    if not os.path.exists(program_path):
        raise FileNotFoundError(f"Program for visualization not found: {program_path}")
    if not os.path.exists(package_path):
        raise FileNotFoundError(f"Package path not found: {package_path}")

    dependencies = parse_dependencies(package_path, max_depth)
    plantuml_script = generate_plantuml_script(dependencies)

    script_path = os.path.join(os.path.dirname(output_path), "dependencies.puml")
    save_plantuml_script(script_path, plantuml_script)

    # Run PlantUML using Java
    java_command = ["java", "-jar", program_path, "-tpng", script_path, "-o", os.path.dirname(output_path)]
    subprocess.run(java_command, check=True)

    print(f"Dependency graph successfully visualized at: {output_path}")


if __name__ == "__main__":
    visualize_dependencies("../env/config.csv")
