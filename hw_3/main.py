import json

from hw_3.src.utils.errors import ConfigurationError
from hw_3.src.utils.generator import generate_output
from hw_3.src.utils.parser import parse_json


def main():
    json_file_path = input("Введите путь к JSON-файлу: ")

    try:
        # Открываем файл по указанному пути
        with open(json_file_path, 'r', encoding="UTF-8") as file:
            json_data = json.load(file)

        if json_data is None:
            raise ConfigurationError(f"Configuration error: Invalid value type: {type(json_data)}")

        # Парсим JSON и генерируем выходной формат
        parsed_data = parse_json(json_data)
        output = generate_output(parsed_data)
        print("Сконвертированный текст в учебном конфигурационном языке:")
        print(output)


    except FileNotFoundError:
        print(f"Error: File '{json_file_path}' not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    except ConfigurationError as e:
        print(f"Configuration error: {e}")


if __name__ == "__main__":
    main()
