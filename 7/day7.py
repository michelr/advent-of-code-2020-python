def parse_contained(bag_line):
    parts = bag_line.split(" ")
    return (parts[1] + parts[2], int(parts[0]))


def parse(row):
    row = row.split("contain")
    color = "".join(row[0].split(" ")[0:2])
    contains = [
        parse_contained(c.strip())
        for c in row[1].split(", ")
        if "no other bags" not in c
    ]
    return (color, contains)


def bags_containing(color, bag_dimensions, bags=set()):
    for col, contained_bags in bag_dimensions.items():
        hits = list(filter(lambda x: x[0] == color, contained_bags))
        if len(hits):
            bags.add(col)
            bags_containing(col, bag_dimensions, bags)
    return bags


def contained_bags(color, bag_dimensions, bags=[]):
    for col, count in bag_dimensions.get(color):
        for _ in range(count):
            bags.append(col)
            contained_bags(col, bag_dimensions, bags)
    return bags


bag_dimensions = {
    parsed[0]: parsed[1]
    for line in open("input.txt").read().split("\n")
    if (parsed := parse(line)) is not None
}
print(len(bags_containing("shinygold", bag_dimensions)))
print(len(contained_bags("shinygold", bag_dimensions)))
