def find_largest_under_max_in_range(line, begin, end, max):
    biggest = -1
    index = -1
    checkable = line[begin:end]
    for id, chr in enumerate(checkable):
        if int(chr) > biggest and int(chr) < max:
            biggest = int(chr)
            index = id + begin
    return index


def main(filename, test, expected):
    lines = []
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    total = 0
    for line in lines:
        indexes = [-1 for _ in range(12)]
        current_index_to_check = 0
        while len(set(indexes)) != 12 or -1 in indexes:  # check if all indexes are different
            smallest_index = indexes[current_index_to_check - 1]+1 if current_index_to_check != 0 else 0
            current_value = int(line[indexes[current_index_to_check]]) if indexes[current_index_to_check] != -1 else 10
            max_index = len(line) - 11 + current_index_to_check
            if max_index - smallest_index < 1:  # we need to pick another value for some earlier indexes
                current_index_to_check -= 1
                continue
            l_index = find_largest_under_max_in_range(line, smallest_index, max_index, current_value)
            if l_index == -1:
                print("didnt find")
                return
            indexes[current_index_to_check] = l_index
            current_index_to_check += 1

        final = sum([int(line[w]) * 10**id for id, w in enumerate(indexes[::-1])])
        if test:
            print(final)
        total += final
    print(total)
    if test:
        print("correct: " + str(total == expected))
        return total == expected
    return None


if __name__ == "__main__":
    if main("day_3/testinput", True, 3121910778619):
        main("day_3/input", False, None)
