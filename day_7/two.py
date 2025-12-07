def read_grid(filename) -> tuple[list[list[str]], int, int]:
    lines = []
    with open(filename, "r") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    height = len(lines)
    width = len(lines[0])
    grid = [[lines[y][x] for x in range(width)] for y in range(height)]
    return grid, width, height


def run_day(filename) -> int:
    grid, width, height = read_grid(filename)
    x_start = grid[0].index("S")
    laser_layers = [dict() for _ in range(height+1)]
    laser_layers[0][x_start] = 1
    for y in range(height):
        for laser_x in laser_layers[y]:
            if grid[y][laser_x] == "^":
                if laser_x+1 not in laser_layers[y+1]:
                    laser_layers[y+1][laser_x+1] = laser_layers[y][laser_x]
                else:
                    laser_layers[y+1][laser_x+1] += laser_layers[y][laser_x]
                if laser_x-1 not in laser_layers[y+1]:
                    laser_layers[y+1][laser_x-1] = laser_layers[y][laser_x]
                else:
                    laser_layers[y+1][laser_x-1] += laser_layers[y][laser_x]
            else:
                if laser_x not in laser_layers[y+1]:
                    laser_layers[y+1][laser_x] = laser_layers[y][laser_x]
                else:
                    laser_layers[y+1][laser_x] += laser_layers[y][laser_x]
    return sum(laser_layers[-1].values())


if __name__ == "__main__":
    test = run_day("day_7/testinput.txt")
    print(test)
    if test == 40:
        print("Running real input")
        real = run_day("day_7/input.txt")
        print(real)
