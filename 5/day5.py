from functools import reduce


def split_seats(prev, next):
    slice_step = (prev[1] - prev[0] + 1) / 2
    if next == "F" or next == "L":
        return (prev[0], prev[1] - slice_step)
    elif next == "B" or next == "R":
        return (prev[0] + slice_step, prev[1])


def calculate_seat_id(boarding_pass):
    row = int(reduce(split_seats, boarding_pass[0:7], (0, 127))[0])
    seat = int(reduce(split_seats, boarding_pass[7:10], (0, 7))[0])
    return row * 8 + seat


seat_ids = list(map(calculate_seat_id, open("input.txt").read().split()))
part1 = max(seat_ids)

seat_ids = sorted(seat_ids)
part2 = [s for s in range(seat_ids[0], seat_ids[-1] + 1) if s not in seat_ids][0]

print(part1)
print(part2)
