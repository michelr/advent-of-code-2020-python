import re
import operator


def is_valid_field(code, value):
    if code == "byr" and (1920 <= int(value) <= 2002):
        return True
    if code == "iyr" and (2010 <= int(value) <= 2020):
        return True
    if code == "eyr" and (2020 <= int(value) <= 2030):
        return True
    if code == "hgt" and re.search(
        r"^((1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in)$", value
    ):
        return True
    if code == "hcl" and re.search(r"^#[\da-f]{6}$", value):
        return True
    if code == "ecl" and re.search(r"^(amb|blu|brn|gry|grn|hzl|oth)$", value):
        return True
    if code == "pid" and re.search(r"^\d{9}$", value):
        return True
    if code == "cid":
        return True


passports = map(
    lambda x: list(map(lambda y: y.split(":"), x)),
    map(
        lambda x: x.replace("\n", " ").split(" "),
        open("input.txt").read().split("\n\n"),
    ),
)

valid_passports = [
    p
    for p in passports
    if set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]).issubset(
        set([i[0] for i in p])
    )
]

part1 = len(valid_passports)
part2 = len(
    list(
        filter(
            operator.truth,
            [
                all(map(lambda x: is_valid_field(x[0], x[1]), vp))
                for vp in valid_passports
            ],
        )
    )
)

print(part1)
print(part2)
