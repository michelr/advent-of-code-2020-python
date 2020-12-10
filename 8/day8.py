def execute(instruction, next, acc):
    op, value = instruction
    if op == "nop":
        next += 1
    elif op == "acc":
        next += 1
        acc += int(value)
    elif op == "jmp":
        next += 1 if int(value) == 0 else int(value)
    return (next, acc)


def run_instructions(instructions):
    next = 0
    acc = 0
    used = []
    aborted = False
    for _ in range(len(instructions) + 1):
        if next == len(instructions):
            return (acc, False)
        if next in used:
            aborted = True
            break
        used.append(next)
        next, acc = execute(instructions[next], next, acc)
    return (acc, aborted)


data = [tuple(line.split()) for line in open("input.txt").read().split("\n")]
print(run_instructions(data)[0])

nop_and_jmp_indexes = [i for i, x in enumerate(data) if x[0] in ["nop", "jmp"]]
total = 0

for i in nop_and_jmp_indexes:
    copy = data.copy()
    op, val = copy[i]
    if op == "nop":
        copy[i] = ("jmp", val)
    elif op == "jmp":
        copy[i] = ("nop", val)
    acc, aborted = run_instructions(copy)
    if not aborted:
        total = acc
        break

print(total)
