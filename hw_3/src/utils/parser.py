from .errors import ConfigurationError

__all__ = [
    "parse_dict",
    "parse_array",
    "parse_value",
    "parse_json"
]

def parse_json(data):
    if isinstance(data, dict):
        return parse_dict(data)
    elif isinstance(data, list):
        return parse_array(data)
    else:
        raise ConfigurationError("Invalid data type at the top level.")

def parse_dict(data):
    output = "begin\n"
    for key, value in data.items():
        output += f" {key} := {parse_value(value)};\n"
    output += "end"
    return output

def parse_array(data):
    return "{ " + " . ".join(parse_value(item) for item in data) + " }"

def parse_value(value):
    if isinstance(value, dict):
        return parse_dict(value)
    elif isinstance(value, list):
        return parse_array(value)
    elif isinstance(value, str):
        return f"'{value}'"
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        raise ConfigurationError(f"Invalid value type: {type(value)}")
