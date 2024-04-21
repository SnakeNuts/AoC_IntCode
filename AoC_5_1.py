from intcode_cpu import IntCodeCPU

with open("AoC_5.txt") as code_input:
    code = list(map(int, code_input.readline().split(",")))

cpu = IntCodeCPU(code)
cpu.run()