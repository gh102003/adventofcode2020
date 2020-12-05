import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")
# lines = []

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def test_passport(file):
    fields_left = required_fields.copy()
    line = None
    while line != "":
        line = file.readline().strip("\n")
        for pair in line.split(" "):
            try:
                fields_left.remove(pair.split(":")[0])
            except ValueError:
                pass

    if len(fields_left) == len(required_fields):
        return None
    if len(fields_left) > 0:
        print("missing:", fields_left)
        return False
    else:
        return True

valid = 0
checked = 0
with open(input_path, "r") as file:
    while (v := test_passport(file)) is not None:
        checked += 1
        if v == True:
            valid += 1

print("checked passports:", checked)
print("valid passports:", valid)
    

