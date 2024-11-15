import json

from hw_4.src.assemble.assembler import assemble
from hw_4.src.interpret.interpretator import interpret


def test_load_const():
    with open('../config/input.asm', 'w') as f:
        f.write('LOAD_CONST A=7 B=414\n')

    assemble('../config/input.asm', 'program.bin', 'log.json')

    interpret('../assemble/program.bin', 'result.json', (0, 10))

    with open('result.json', 'r') as f:
        result = json.load(f)

    assert result['accumulator'] == 0
    assert result['memory_range'] == [0] * 10
