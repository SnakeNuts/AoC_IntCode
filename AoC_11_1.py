from intcode_cpu import IntCodeCPU
from collections import defaultdict

with open("AoC_11.txt") as code_input:
    code = list(map(int, code_input.readline().split(",")))

robot_CPU = IntCodeCPU(code)
robot_CPU.input_mode = 1
robot_CPU.output_mode = 2

hull = defaultdict(int)

finished = False
X = 0
Y = 0
while not finished:
    tile = hull[(X, Y)]
    robot_CPU.input_buffer.put_nowait(tile)
    robot_CPU.run()
    if robot_CPU.exited:
        finished = True
        continue
    paint = robot_CPU.output_buffer
    if paint