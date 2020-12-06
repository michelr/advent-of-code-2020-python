from collections import Counter
from functools import reduce

result = sum(
    [
        len(set("".join(group.split("\n"))))
        for group in open("input.txt").read().split("\n\n")
    ]
)
print(str.format("Part1: {}", result))


def all_items_letters(items):
    if len(items) == 1:
        return len(items[0])
    else:
        return sum(reduce(lambda x, y: Counter(x) & Counter(y), items).values())


result = sum(
    [
        all_items_letters(group.split("\n"))
        for group in open("input.txt").read().split("\n\n")
    ]
)
print(str.format("Part2: {}", result))
