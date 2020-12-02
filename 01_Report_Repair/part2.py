import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

entries = []

with open(input_path, "r") as file:
    for line in file:
        entries.append(int(line))

for a in entries:
    for b in entries:
        for c in entries:
            if a + b + c == 2020:
                print(f"{a} + {b} + {c} = {a + b + c}")
                print(f"{a} * {b} * {c} = {a * b * c}")
