import struct
import json

def interpret(input_file, output_file, memory_range=(0,10)):
    memory = [0] * 1024  # Примерный размер памяти
    accumulator = 0

    with open(input_file, 'rb') as f:
        bytecode = f.read()

    i = 0
    while i < len(bytecode):
        opcode = bytecode[i]
        b = struct.unpack('>H', bytecode[i+1:i+3])[0]
        a = bytecode[i+3]
        i += 4

        if opcode == 0xF7:  # LOAD_CONST
            accumulator = a
        elif opcode == 0xFB:  # READ
            accumulator = memory[b]
        elif opcode == 0x9C:  # WRITE
            memory[b] = accumulator
        elif opcode == 0x5A:  # SHIFT_RIGHT
            memory[b] = accumulator >> 1
        else:
            continue

    # Записываем результаты в json
    result = {
        "memory_range": memory[memory_range[0]:memory_range[1]],
        "accumulator": accumulator
    }

    with open(output_file, 'w') as f:
        json.dump(result, f, indent=4)

if __name__ == '__main__':
    interpret("../assemble/program.bin",  "result.json")