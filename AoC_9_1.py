from intcode_cpu import IntCodeCPU

with open("AoC_9.txt") as code_input:
    code = list(map(int, code_input.readline().split(",")))

cpu = IntCodeCPU(code)
cpu.run()
