from intcode_cpu import IntCodeCPU

count = 0

def draw_pixel(x, y, tile_id):
    global count
    print(f"Drawing {tile_id} at ({x}, {y})")
    if tile_id == 2:
        count += 1



with open("AoC_13.txt") as code_input:
    code = list(map(int, code_input.readline().split(",")))

CPU = IntCodeCPU(code)
CPU.output_mode = 2

input_part = 0
x = 0
y = 0
tile_id = 0
while True:
    CPU.run()
    if CPU.exited:
        break
    if input_part == 0:
        x = CPU.output_buffer
        input_part = 1
    elif input_part == 1:
        y = CPU.output_buffer
        input_part = 2
    elif input_part == 2:
        tile_id = CPU.output_buffer
        input_part = 0
        draw_pixel(x, y, tile_id)

print(count)