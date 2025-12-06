import numpy as np


def run_day(filename) -> int:
    total = 0

    with open(filename, 'r') as file:
        lines = file.readlines()
    split_lines = [[x for x in line] for line in lines]
    split_lines[-1].append(" ")
    stacked = np.vstack(split_lines)
    stacked = np.rot90(stacked, k=1, axes=(0, 1))

    this_sum = ''
    current_operator = ""
    for index in range(len(stacked)-1, 0, -1):
        num = ''.join(stacked[index])
        if num.strip() == "":
            continue
        if num[-1] in ["*", "+"]:
            if this_sum != "":
                this_sum = this_sum[:-1]
                total += eval(this_sum)
            this_sum = ""
            current_operator = num[-1]
            this_sum += num
        else:
            this_sum += num
            this_sum += current_operator

    if this_sum != "":
        this_sum = this_sum[:-1]
        total += eval(this_sum)

    return total


if __name__ == "__main__":
    real = run_day("day_6/input.txt")
    print(f"real output: {real}")
    quit()
