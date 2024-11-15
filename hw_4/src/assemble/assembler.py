import struct
import json


def assemble(input_file, output_file, log_file):
    instructions = []
    with open(input_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        command = parts[0]
        params = dict(param.split('=') for param in parts[1:])

        if command == "LOAD_CONST":
            a = int(params['A'])
            b = int(params['B'])
            instruction = struct.pack('>BBBB', 0xF7, (b >> 8) & 0xFF, b & 0xFF, a)
        elif command == "READ":
            a = int(params['A'])
            b = int(params['B'])
            instruction = struct.pack('>BBBB', 0xFB, (b >> 8) & 0xFF, b & 0xFF, a)
        elif command == "WRITE":
            a = int(params['A'])
            b = int(params['B'])
            instruction = struct.pack('>BBBB', 0x9C, (b >> 8) & 0xFF, b & 0xFF, a)
        elif command == "SHIFT_RIGHT":
            a = int(params['A'])
            b = int(params['B'])
            instruction = struct.pack('>BBBB', 0x5A, (b >> 8) & 0xFF, b & 0xFF, a)
        else:
            continue

        instructions.append(instruction)

    with open(output_file, 'wb') as f:
        for instruction in instructions:
            f.write(instruction)

    # Log the assembly
    log_data = {f"command_{i + 1}": line.strip() for i, line in enumerate(lines)}
    with open(log_file, 'w') as log:
        json.dump(log_data, log, indent=4)

if __name__ == '__main__':
    assemble("../config/input.asm", "program.bin", "log_assemble.json")