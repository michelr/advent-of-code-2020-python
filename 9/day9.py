from itertools import combinations
from functools import reduce


numbers = [int(line) for line in open("input.txt").read().split("\n")]

parts = [
    numbers[i : i + 26] for i in range(len(numbers) + 26) if len(numbers) >= i + 26
]


def valid(numbers):
    val = numbers[25]
    return (val, any((sum(c) == val for c in combinations(numbers[0:25], 2))))


invalid_no, _ = list(filter(lambda x: not x[1], map(valid, parts)))[0]


def less_or_equal(x, y, result):

    if sum(x) < result and y != result:
        x.append(y)
    return x


contiguous = sorted(
    list(
        filter(
            lambda x: sum(x) == invalid_no,
            [
                reduce(lambda x, y: less_or_equal(x, y, invalid_no), numbers[i:], [])
                for i in range(len(numbers) + 1)
            ],
        )
    )[0]
)

weakness = contiguous[0] + contiguous[-1]
print(invalid_no)
print(weakness)
