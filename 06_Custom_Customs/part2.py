import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

answer = 0

with open(input_path, "r") as file:
  current_group = None
  for line in file:
    line = line.rstrip("\n")
    if line == "":
      answer += len(current_group)
      current_group = None
    else:
      if current_group is None:
        current_group = set(line)
      else:
        current_group = current_group.intersection(set(line))
        
  answer += len(current_group)
  current_group = set()
  
print("answer:", answer)