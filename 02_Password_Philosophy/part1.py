import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

lines = []

with open(input_path, "r") as file:
    for line in file:
      lines.append(line)

valid_passwords = 0

for line in lines:
  count_range, character, password = line.replace(":", "").split(" ")
  count_min, count_max = count_range.split("-")

  count_password = password.count(character)

  if int(count_min) <= count_password <= int(count_max):
    valid_passwords += 1

print(valid_passwords, "valid passwords")