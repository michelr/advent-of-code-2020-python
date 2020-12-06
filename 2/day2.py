def create_item(row):
    items = row.split(" ")
    pwd_pattern = items[0].split("-")
    return {
        "first": int(pwd_pattern[0]),
        "second": int(pwd_pattern[1]),
        "character": items[1].replace(":", ""),
        "password": items[2],
    }


def in_range(min, max, character, password):
    no_of_times = len([c for c in password if character == c])
    return min <= no_of_times <= max


def in_position(first, second, character, password):
    isFirst = password[first - 1] == character
    isSecond = password[second - 1] == character
    return isFirst != isSecond


policies = [create_item(line) for line in open("input.txt").read().split("\n")]

part1 = len(
    [
        p
        for p in policies
        if in_range(p["first"], p["second"], p["character"], p["password"])
    ]
)

part2 = len(
    [
        p
        for p in policies
        if in_position(p["first"], p["second"], p["character"], p["password"])
    ]
)

print(part1)
print(part2)
