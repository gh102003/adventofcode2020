import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

numbers = []

with open(input_path, "r") as file:
    for num in file:
        numbers.append(int(num.rstrip("\n")))

def test_index(i):
    current = numbers[i]
    prev_25 = numbers[i-25:i]
    
    for j in prev_25:
        for k in prev_25:
            if j + k == current:
                return True
    
    return False

for i in range(25, len(numbers)):
    if not test_index(i):
        print(numbers[i])