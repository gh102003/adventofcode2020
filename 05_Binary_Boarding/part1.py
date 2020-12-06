import os
input_path = os.path.join(os.path.dirname(__file__), "input.txt")

def get_seat_id(column, row):
    return row * 8 + column

max_seat_id = 0

with open(input_path, "r") as file:
    for line in file:
        row_binary = line[:7].replace("F", "0").replace("B", "1")
        row = int(row_binary, 2)

        column_binary = line[7:].replace("L", "0").replace("R", "1")
        column = int(column_binary, 2)

        seat_id = get_seat_id(column, row)

        max_seat_id = max(max_seat_id, seat_id)

        print(f"{row=} {column=} {seat_id=}")

print(f"{max_seat_id=}")
