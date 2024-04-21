def get_digit(number, n):
    return number // 10**n % 10


class IntCodeCPU:

    def __init__(self, program: list[int]) -> None:
        self.program = program
        self.instruction_pointer = 0

    # make this into 'read_values(count)' which returns a tuple of 'count' ints and can be used to multi-assign
    def read_next_value(self) -> int:
        value = self.program[self.instruction_pointer]
        self.instruction_pointer += 1
        return value

    def parse_instruction(self, instruction: int) -> None:
        opcode = get_digit(instruction, 0) + (get_digit(instruction, 1) * 10)
        param_1_mode = get_digit(instruction, 2)
        param_2_mode = get_digit(instruction, 3)
        param_3_mode = get_digit(instruction, 4)

        return opcode, param_1_mode, param_2_mode, param_3_mode

    def read_position(self, address: int) -> int:
        return self.program[address]

    def write_position(self, address: int, value: int) -> None:
        self.program[address] = value

    def read(self, param, param_mode):
        if param_mode == 0:
            return self.read_position(param)
        elif param_mode == 1:
            return param
        else:
            raise Exception("Unknown param mode")

    def opcode_add(self, param_1_mode, param_2_mode, param_3_mode) -> None:
        param1 = self.read(self.read_next_value(), param_1_mode)
        param2 = self.read(self.read_next_value(), param_2_mode)
        param3 = self.read_next_value()

        self.write_position(param3, (param1 + param2))

    def opcode_multiply(self, param_1_mode, param_2_mode, param_3_mode) -> None:
        param1 = self.read(self.read_next_value(), param_1_mode)
        param2 = self.read(self.read_next_value(), param_2_mode)
        param3 = self.read_next_value()

        self.write_position(param3, (param1 * param2))

    def opcode_input(self, param_1_mode, param_2_mode, param_3_mode) -> None:
        param1 = self.read_next_value()

        self.write_position(param1, int(input("Please input number:")))

    def opcode_output(self, param_1_mode, param_2_mode, param_3_mode) -> None:
        param1 = self.read(self.read_next_value(), param_1_mode)

        print(param1)

    def opcode_jump_if_true(self, param_1_mode, param_2_mode, param_3_mode) -> None:
        param1 = self.read(self.read_next_value(), param_1_mode)
        param2 = self.read(self.read_next_value(), param_2_mode)

        if param1 != 0:
            self.instruction_pointer = param2

    def opcode_jump_if_false(self, param_1_mode, param_2_mode, param_3_mode) -> None:
        param1 = self.read(self.read_next_value(), param_1_mode)
        param2 = self.read(self.read_next_value(), param_2_mode)

        if param1 == 0:
            self.instruction_pointer = param2

    def opcode_less_than(self, param_1_mode, param_2_mode, param_3_mode) -> None:
        param1 = self.read(self.read_next_value(), param_1_mode)
        param2 = self.read(self.read_next_value(), param_2_mode)
        param3 = self.read_next_value()

        if param1 < param2:
            self.write_position(param3, 1)
        else:
            self.write_position(param3, 0)

    def opcode_equals(self, param_1_mode, param_2_mode, param_3_mode) -> None:
        param1 = self.read(self.read_next_value(), param_1_mode)
        param2 = self.read(self.read_next_value(), param_2_mode)
        param3 = self.read_next_value()

        if param1 == param2:
            self.write_position(param3, 1)
        else:
            self.write_position(param3, 0)

    def run(self) -> None:
        while True:
            opcode, param_1_mode, param_2_mode, param_3_mode = self.parse_instruction(
                self.read_next_value()
            )

            match opcode:
                case 99:
                    break
                case 1:
                    self.opcode_add(param_1_mode, param_2_mode, param_3_mode)
                case 2:
                    self.opcode_multiply(param_1_mode, param_2_mode, param_3_mode)
                case 3:
                    self.opcode_input(param_1_mode, param_2_mode, param_3_mode)
                case 4:
                    self.opcode_output(param_1_mode, param_2_mode, param_3_mode)
                case 5:
                    self.opcode_jump_if_true(param_1_mode, param_2_mode, param_3_mode)
                case 6:
                    self.opcode_jump_if_false(param_1_mode, param_2_mode, param_3_mode)
                case 7:
                    self.opcode_less_than(param_1_mode, param_2_mode, param_3_mode)
                case 8:
                    self.opcode_equals(param_1_mode, param_2_mode, param_3_mode)
                case _:
                    print("Illegal Opcode")

        print("Program finished")

    def dump_memory(self) -> None:
        print(",".join(list(map(str, self.program))))

    def print_memory_location(self, address: int) -> None:
        print(self.read_position(address))


if __name__ == "__main__":
    test_CPU = IntCodeCPU([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
    test_CPU.run()
    test_CPU.dump_memory()
