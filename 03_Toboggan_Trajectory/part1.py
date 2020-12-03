import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

rows = []
with open(input_path) as file:
  for line in file:
    rows.append(line.rstrip("\n"))
    
#print(rows)

def check_slope(x_step, y_step):
  trees = 0
  
  x_pos = 0
  y_pos = 0
  while y_pos < len(rows):
    if rows[y_pos][x_pos] == "#":
      trees += 1
    
    x_pos += x_step
    y_pos += y_step
    x_pos %= len(rows[0])
  
  return trees
  
print(check_slope(1, 1))
print(check_slope(3, 1)) # part 1
print(check_slope(5, 1))
print(check_slope(7, 1))
print(check_slope(1, 2))

print(check_slope(1, 1) * check_slope(3, 1) * check_slope(5, 1) * check_slope(7, 1) * check_slope(1, 2))