def read_grid(filename) -> tuple[list[list[str]], int, int]:
    lines = []
    with open(filename, "r") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    height = len(lines)
    width = len(lines[0])
    grid = [[lines[y][x] for x in range(width)] for y in range(height)]
    return grid, width, height


def get_all_neighbors_from_cell(grid, x, y, width, height) -> list[tuple[int, int]]:
    all_pos: list[tuple[int, int]] = []
    for y_offset in (-1, 0, 1):
        for x_offset in (-1, 0, 1):
            if x_offset == 0 and y_offset == 0:
                continue
            if x + x_offset < 0 or x + x_offset >= width:
                continue
            if y + y_offset < 0 or y + y_offset >= height:
                continue
            all_pos.append((x + x_offset, y + y_offset))

    return all_pos


def run_day(filename) -> int:
    grid, width, height = read_grid(filename)
    total_rolls = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] != "@":
                continue
            neighbor_posses = get_all_neighbors_from_cell(grid, x, y, width, height)
            total_n = 0
            for pos in neighbor_posses:
                if grid[pos[1]][pos[0]] == "@":
                    total_n += 1
            if total_n < 4:
                total_rolls += 1

    return total_rolls


if __name__ == "__main__":
    test = run_day("day_4/testinput.txt")
    print(test)
    if test == 13:
        print("Running real input")
        real = run_day("day_4/input.txt")
        print(real)
