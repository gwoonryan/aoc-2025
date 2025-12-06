def run_day(filename) -> int:
    total = 0
    formulas = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    for line in lines:
        offset = 0
        for id, num in enumerate(line.split(" ")):
            if len(formulas) <= id + offset:
                formulas.append([])
            if num == "":
                offset -= 1
                continue
            formulas[id + offset].append(num)
    print(formulas)

    for formula in formulas:
        full = ""
        for item in formula[:-1]:
            full += item
            full += formula[-1]
        full = full[:-1]
        print(full)
        total += eval(full)

    return total


if __name__ == "__main__":
    test = run_day("day_6/testinput.txt")
    print(f"test output: {test}")
    if test == 4277556:
        print("Running real input")
        real = run_day("day_6/input.txt")
        print(f"real output: {real}")
