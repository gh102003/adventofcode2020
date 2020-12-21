import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

instructions = []

with open(input_path, "r") as file:
    for instruction in file:
        instructions.append(instruction)

accumulator = 0
pc = 0
executed = []

while pc < len(instructions):
    if pc in executed:
        break

    print(pc)
    executed.append(pc)

    opcode, operand = instructions[pc].split(" ")
    if opcode == "jmp":
        pc += int(operand)
    else:
        pc += 1

    if opcode == "acc":
        accumulator += int(operand)


print(f"{accumulator=}")
