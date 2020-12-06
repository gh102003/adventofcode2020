import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def get_seat_id(column, row):
    return row * 8 + column

seats_empty = list(range(128*8))

with open(input_path, "r") as file:
    for line in file:
        row_binary = line[:7].replace("F", "0").replace("B", "1")
        row = int(row_binary, 2)

        column_binary = line[7:].replace("L", "0").replace("R", "1")
        column = int(column_binary, 2)

        seat_id = get_seat_id(column, row)

        seats_empty.remove(seat_id)

print(seats_empty)

for seat_id in seats_empty:
  if not (seat_id - 1 in seats_empty or seat_id + 1 in seats_empty):
    print(seat_id)