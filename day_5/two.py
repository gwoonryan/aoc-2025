def in_range(begin, end, item):
    return begin <= item and end >= item


def run_day(filename) -> int:
    total = 0
    ranges = []
    items = []
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
    first = True
    for line in lines:
        if line == "":
            first = False
            continue
        if first:
            ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))
        else:
            items.append(int(line))

    for item in items:
        in_a_range = False
        for range in ranges:
            if in_range(range[0], range[1], item):
                in_a_range = True
                break
        if in_a_range:
            total += 1

    return total


if __name__ == "__main__":
    test = run_day("day_5/testinput.txt")
    print(test)
    if test == 3:
        print("Running real input")
        real = run_day("day_5/input.txt")
        print(real)
