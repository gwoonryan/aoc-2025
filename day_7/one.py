def read_grid(filename) -> tuple[list[list[str]], int, int]:
    lines = []
    with open(filename, "r") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    height = len(lines)
    width = len(lines[0])
    grid = [[lines[y][x] for x in range(width)] for y in range(height)]
    return grid, width, height


# def get_all_neighbors_from_cell(grid, x, y, width, height) -> list[tuple[int, int]]:
#     all_pos: list[tuple[int, int]] = []
#     for y_offset in (-1, 0, 1):
#         for x_offset in (-1, 0, 1):
#             if x_offset == 0 and y_offset == 0:
#                 continue
#             if x + x_offset < 0 or x + x_offset >= width:
#                 continue
#             if y + y_offset < 0 or y + y_offset >= height:
#                 continue
#             all_pos.append((x + x_offset, y + y_offset))

#     return all_pos


def run_day(filename) -> int:
    grid, width, height = read_grid(filename)
    total_splits = 0
    x_start = grid[0].index("S")
    laser_layers = [set() for _ in range(height+1)]
    laser_layers[0].add(x_start)
    for y in range(height):
        for laser_x in laser_layers[y]:
            if grid[y][laser_x] == "^":
                laser_layers[y+1].add(laser_x+1)
                laser_layers[y+1].add(laser_x-1)
                total_splits += 1
            else:
                laser_layers[y+1].add(laser_x)
    return total_splits


if __name__ == "__main__":
    test = run_day("day_7/testinput.txt")
    print(test)
    if test == 21:
        print("Running real input")
        real = run_day("day_7/input.txt")
        print(real)
