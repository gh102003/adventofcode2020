import os
import re
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

rules = {}
with open(input_path, "r") as file:
    rules = {line.split("bags contain")[0].strip(" .\n"): line.split(
        "contain")[1].strip(" .\n") for line in file}


def can_contain_shiny_gold(bag, depth=0):
    # print(" " * depth, bag)
    if bag == "shiny gold":
        return True

    contents = rules[bag]

    if contents == "no other bags":
        return False
    if "shiny gold" in contents:
        return True
    else:
        for match in re.finditer(r"[1-9]+ ([a-z]+ [a-z]+) bags", contents):
            if can_contain_shiny_gold(match.group(1), depth+1):
                return True

    return False


# print(rules)
# print()

total = 0
for bag in rules.keys():
    if can_contain_shiny_gold(bag):
        total += 1
        print(f"{bag} can contain shiny gold\n")
    else:
        print(f"{bag} cannot contain shiny gold\n")

print(f"{total=}")
