from itertools import combinations
from functools import reduce
import operator


def multiply_reports(no_of_expenses, expenses):
    return [
        reduce(operator.mul, c)
        for c in combinations([int(row) for row in expenses], no_of_expenses)
        if sum(list(c)) == 2020
    ][0]


expenses = open("input.txt").read().split()
print(multiply_reports(2, expenses))
print(multiply_reports(3, expenses))
