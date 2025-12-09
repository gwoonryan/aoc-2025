# def point_distance(p1, p2):
#     return sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2) + ((p1[2] - p2[2]) ** 2))


def run_day(filename) -> int:
    points = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    for line in lines:
        points.append(tuple([int(num) for num in line.split(",")]))

    largest = 0
    l_p1 = None
    l_p2 = None
    for p1 in points:
        for p2 in points:
            x_min = min(p1[0], p2[0])
            x_max = max(p1[0], p2[0]) + 1
            y_min = min(p1[1], p2[1])
            y_max = max(p1[1], p2[1]) + 1
            area = (x_max - x_min) * (y_max - y_min)
            if area > largest:
                l_p1 = p1
                l_p2 = p2
                largest = area
    print(l_p1)
    print(l_p2)
    return largest


if __name__ == "__main__":

    test = run_day("day_9/testinput.txt")
    print(f"test output: {test}")
    if test == 50:
        print("Running real input")
        real = run_day("day_9/input.txt")
        print(f"real output: {real}")
