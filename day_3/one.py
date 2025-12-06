def main(filename, test):
    lines = []
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    total = 0
    for line in lines:
        biggest_first = 0
        biggest_index = 0

        for id, chr in enumerate(line[:-1]):
            if int(chr) > biggest_first:
                biggest_first = int(chr)
                biggest_index = id

        biggest_second = 0
        for chr in line[biggest_index+1:]:
            if int(chr) > biggest_second:
                biggest_second = int(chr)

        final = biggest_first * 10 + biggest_second
        if test:
            print(final)
        total += final
    print(total)
    print("\n")


if __name__ == "__main__":
    main("day_3/testinput", True)
    main("day_3/input", False)
