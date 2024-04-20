class IntCodeCPU:

    def __init__(self, program: list[int]) -> None:
        self.program = program
        self.instruction_pointer = 0

    # make this into 'read_values(count)' which returns a tuple of 'count' ints and can be used to multi-assign
    def read_next_value(self) -> int:
        value = self.program[self.instruction_pointer]
        self.instruction_pointer += 1
        return value

    def read_immediate(self, address: int) -> int:
        return self.program[address]
    
    def write_immediate(self, address: int, value: int) -> None:
        self.program[address] = value

    def opcode_add(self) -> None:
        param1 = self.read_next_value()
        param2 = self.read_next_value()
        param3 = self.read_next_value()

        self.write_immediate(param3, (self.read_immediate(param1) + self.read_immediate(param2)))

    def opcode_multiply(self) -> None:
        param1 = self.read_next_value()
        param2 = self.read_next_value()
        param3 = self.read_next_value()

        self.write_immediate(param3, (self.read_immediate(param1) * self.read_immediate(param2)))

    def run(self) -> None:
        while True:
            current_opcode = self.read_next_value()
            match current_opcode:
                case 99:
                    break
                case 1:
                    self.opcode_add()
                case 2:
                    self.opcode_multiply()
                case _:
                    print("Illegal Opcode")

        print("Program finished")

    def dump_memory(self) -> None:
        print(",".join(list(map(str, self.program))))

    def print_memory_location(self, address: int) -> None:
        print(self.read_immediate(address))


if __name__ == "__main__":
    test_CPU = IntCodeCPU([1,9,10,3,2,3,11,0,99,30,40,50])
    test_CPU.run()
    test_CPU.dump_memory()
