from intcode_cpu import IntCodeCPU

with open("AoC_1.txt") as code_input:
    code = list(map(int, code_input.readline().split(",")))

cpu = IntCodeCPU(code)
cpu.write_immediate(1, 12)
cpu.write_immediate(2, 2)
cpu.run()
cpu.print_memory_location(0)