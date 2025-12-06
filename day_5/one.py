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

    changed = True
    while changed:
        to_be_removed_new = []
        to_be_added_new = []
        changed = False
        # print(f"begin list: {ranges}")
        for id_1, range_1 in enumerate(ranges):
            for id_2, range_2 in enumerate(ranges):
                if id_1 == id_2:
                    continue
                if in_range(range_1[0], range_1[1], range_2[0]) and in_range(range_1[0], range_1[1], range_2[1]):
                    to_be_removed_new.append(range_2)
                    changed = True
                    break
                elif in_range(range_1[0], range_1[1], range_2[0]) and (not in_range(range_1[0], range_1[1], range_2[1])):
                    # first half contained
                    to_be_removed_new.append(range_1)
                    to_be_removed_new.append(range_2)
                    to_be_added_new.append((range_1[0], range_2[1]))
                    changed = True
                    break
                elif (not in_range(range_1[0], range_1[1], range_2[0])) and in_range(range_1[0], range_1[1], range_2[1]):
                    # second half contained
                    to_be_removed_new.append(range_1)
                    to_be_removed_new.append(range_2)
                    to_be_added_new.append((range_2[0], range_1[1]))
                    changed = True
                    break
            if changed:
                break
        # print(f"rem: {to_be_removed_new}")
        # print(f"add: {to_be_added_new}")
        for rem in set(to_be_removed_new):
            ranges.remove(rem)
        for ad in set(to_be_added_new):
            ranges.append(ad)
        # print(f"new list: {ranges}")
        # print("\n")

    for range_ in ranges:
        total += range_[1] - range_[0] + 1

    return total


if __name__ == "__main__":
    test = run_day("day_5/testinput.txt")
    print(test)
    if test == 14:
        print("Running real input")
        real = run_day("day_5/input.txt")
        print(real)
