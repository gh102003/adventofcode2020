import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

instructions = []

with open(input_path, "r") as file:
    for instruction in file:
        instructions.append(instruction.rstrip("\n"))


def terminates(instructions):
    accumulator = 0
    pc = 0
    executed = []

    while pc < len(instructions):
        if pc in executed:
            return "pc in executed"

        # print(pc)
        executed.append(pc)

        opcode, operand = instructions[pc].split(" ")
        if opcode == "jmp":
            pc += int(operand)
        else:
            pc += 1

        if opcode == "acc":
            accumulator += int(operand)
    
    return accumulator


for i, instruction in enumerate(instructions):
    opcode, operand = instruction.split(" ")
    
    if opcode == "acc":
        continue

    # print(i)

    instructions_copy = instructions.copy()
    if opcode == "jmp":
        instructions_copy[i] = "nop " + operand
    elif opcode == "nop":
        instructions_copy[i] = "jmp " + operand

    # print(instructions[i], "=>", instructions_copy[i])

    result = terminates(instructions_copy)
    if result != "pc in executed":
        print()
        print(result)
        break

# print(f"{accumulator=}")
