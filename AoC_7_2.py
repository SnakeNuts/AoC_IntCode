from intcode_cpu import IntCodeCPU
from copy import deepcopy
import itertools


with open("AoC_7.txt") as code_input:
    code = list(map(int, code_input.readline().split(",")))

settings = [5, 6, 7, 8, 9]

permutations = itertools.permutations(settings)

thruster_signal = 0

for permutation in permutations:
    print(permutation)

    cpu_A = IntCodeCPU(deepcopy(code))
    cpu_A.set_input_mode(1)
    cpu_A.set_output_mode(2)
    cpu_A.add_input_value(permutation[0])
    cpu_B = IntCodeCPU(deepcopy(code))
    cpu_B.set_input_mode(1)
    cpu_B.set_output_mode(2)
    cpu_B.add_input_value(permutation[1])
    cpu_C = IntCodeCPU(deepcopy(code))
    cpu_C.set_input_mode(1)
    cpu_C.set_output_mode(2)
    cpu_C.add_input_value(permutation[2])
    cpu_D = IntCodeCPU(deepcopy(code))
    cpu_D.set_input_mode(1)
    cpu_D.set_output_mode(2)
    cpu_D.add_input_value(permutation[3])
    cpu_E = IntCodeCPU(deepcopy(code))
    cpu_E.set_input_mode(1)
    cpu_E.set_output_mode(2)
    cpu_E.add_input_value(permutation[4])

    loopback_value = 0
    finished = False
    while not finished:

        cpu_A.add_input_value(loopback_value)
        cpu_A.run()
        output_cpu_A = cpu_A.output_buffer
        exit_state_cpu_A = cpu_A.exited

        cpu_B.add_input_value(output_cpu_A)
        cpu_B.run()
        output_cpu_B = cpu_B.output_buffer
        exit_state_cpu_B = cpu_B.exited

        cpu_C.add_input_value(output_cpu_B)
        cpu_C.run()
        output_cpu_C = cpu_C.output_buffer
        exit_state_cpu_C = cpu_C.exited

        cpu_D.add_input_value(output_cpu_C)
        cpu_D.run()
        output_cpu_D = cpu_D.output_buffer
        exit_state_cpu_D = cpu_D.exited

        cpu_E.add_input_value(output_cpu_D)
        cpu_E.run()
        output_cpu_E = cpu_E.output_buffer
        exit_state_cpu_E = cpu_E.exited

        loopback_value = output_cpu_E

        if exit_state_cpu_E is True:
            finished = True
            if output_cpu_E > thruster_signal:
                thruster_signal = output_cpu_E

print(thruster_signal)