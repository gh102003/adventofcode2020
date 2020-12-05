import os
import re
input_path = os.path.join(os.path.dirname(__file__), "input.txt")


def validate_passport(passport):
    print(passport)
    try:
        # byr, iyr and eyr
        if not 1920 <= int(passport["byr"]) <= 2002:
            return False
        if not 2010 <= int(passport["iyr"]) <= 2020:
            return False
        if not 2020 <= int(passport["eyr"]) <= 2030:
            return False

        # hgt
        hgt_units = passport["hgt"][-2:]
        hgt_value = passport["hgt"][:-2]
        if hgt_units == "cm":
            if not 150 <= int(hgt_value) <= 193:
                return False
        elif hgt_units == "in":
            if not 59 <= int(hgt_value) <= 76:
                return False
        else:
            return False

        if not re.match(r"^#[0-9a-f]{6}$", passport["hcl"]):
            return False

        if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

        if not re.match(r"^[0-9]{9}$", passport["pid"]):
            return False

    except KeyError:
        return False
    except ValueError:
        return False

    print("valid")

    return True


valid = 0
with open(input_path, "r") as file:
    current_passport = {}
    for line in file:
        if line == "" or line == "\n":
            if validate_passport(current_passport):
                valid += 1
            current_passport = {}
        else:
            for pair in line.rstrip("\n").split(" "):
                k, v = pair.split(":")
                current_passport[k] = v

    # final line
    if validate_passport(current_passport):
        valid += 1

print("Valid:", valid)
