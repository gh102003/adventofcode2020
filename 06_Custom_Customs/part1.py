import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

answer = 0

with open(input_path, "r") as file:
  current_group = set()
  for line in file:
    line = line.rstrip("\n")
    if line == "":
      answer += len(current_group)
      current_group = set()
    else:
      for c in line:
        current_group.add(c)
        
  answer += len(current_group)
  current_group = set()
  
print(answer)