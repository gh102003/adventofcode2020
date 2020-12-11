import os
import re
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

rules = []
with open(input_path, "r") as file:
  rules = {line.split("contain")[0].strip(" .\n"): line.split("contain")[1].strip(" .\n") for line in file}

def can_contain_shiny_gold(bag):
  if bag == "shiny_gold":
    return True
    
  contents = rules[bag]

  if contents == "no other bags":
    return False

print(rules)

# with open(input_path, "r") as file:
  # for rule in file:
    #print(rule.split("contain")[1].rstrip("\n"))
    # for bag in can_contain_shiny_gold:
    #   if re.search(bag, rule.split("contain")[1].rstrip("\n")):
    #     can_contain_shiny_gold.append(rule.split(" bags contain")[0])

print(set(can_contain_shiny_gold))