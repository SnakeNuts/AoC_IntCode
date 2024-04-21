from intcode_cpu import IntCodeCPU
from copy import deepcopy

with open("AoC_2.txt") as code_input:
    code = list(map(int, code_input.readline().split(",")))

for noun in range(0,100):
    for verb in range(0, 100):
        cpu = IntCodeCPU(deepcopy(code))
        cpu.write_position(1, noun)
        cpu.write_position(2, verb)
        cpu.run()
        if cpu.read_position(0) == 19690720:
            print(f"Noun is {noun}, verb is {verb}, 100 * noun + verb is {100 * noun + verb}")
            exit(0)