import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

numbers = []

with open(input_path, "r") as file:
    for num in file:
        numbers.append(int(num.rstrip("\n")))
        
target = 144381670

for j in range(len(numbers) - 1):
    for k in range(j + 1, len(numbers)):
        if sum(numbers[j:k]) == target:
            print(f"{j}-{k-1}, min={min(numbers[j:k])} max={max(numbers[j:k])} sum={min(numbers[j:k]) + max(numbers[j:k])}")