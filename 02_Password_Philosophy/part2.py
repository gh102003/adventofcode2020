import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []

with open(input_path, "r") as file:
    for line in file:
      lines.append(line)

valid_passwords = 0

for line in lines:
  pos_range, character, password = line.replace(":", "").split(" ")
  pos_1, pos_2 = pos_range.split("-")

  at_pos_1 = password[int(pos_1) - 1]
  at_pos_2 = password[int(pos_2) - 1]

  if (at_pos_1 == character) ^ (at_pos_2 == character):
    valid_passwords += 1

print(valid_passwords, "valid passwords")