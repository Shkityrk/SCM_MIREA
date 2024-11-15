import os


def parse_dependencies(package_path, max_depth):
    dependencies = {}
    visited = set()

    def helper(path, depth):
        if depth > max_depth or path in visited:
            return
        visited.add(path)

        if not os.path.isdir(path):
            return

        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                dependencies[path] = dependencies.get(path, []) + [item_path]
                helper(item_path, depth + 1)

    helper(package_path, 0)
    return dependencies


def generate_plantuml_script(dependencies):
    lines = ["@startuml"]
    for parent, children in dependencies.items():
        for child in children:
            lines.append(f'"{os.path.basename(parent)}" --> "{os.path.basename(child)}"')
    lines.append("@enduml")
    return "\n".join(lines)


def save_plantuml_script(filepath, script):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(script)
