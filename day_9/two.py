from tqdm import tqdm


def a_line_passes_through_square(p1, p2, points):
    x_min = min(p1[0], p2[0])
    x_max = max(p1[0], p2[0])
    y_min = min(p1[1], p2[1])
    y_max = max(p1[1], p2[1])
    for id_1, l1 in enumerate(points):
        l2 = points[id_1 + 1 if id_1 + 1 < len(points) else 0]
        if l1[0] == l2[0]:
            line_y_min = min(l1[1], l2[1])
            line_y_max = max(l1[1], l2[1])
            if l1[0] > x_min and l1[0] < x_max:
                if line_y_min < y_min and line_y_max > y_min:
                    return True
                if line_y_min < y_max and line_y_max > y_min:
                    return True
        elif l1[1] == l2[1]:
            line_x_min = min(l1[0], l2[0])
            line_x_max = max(l1[0], l2[0])
            if l1[1] > y_min and l1[1] < y_max:
                if line_x_min < x_min and line_x_max > x_min:
                    return True
                if line_x_min < x_max and line_x_max > x_min:
                    return True
        else:
            assert 1 == 0
    return False


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
    with tqdm(total=len(points) ** 2) as pbar:
        for id1, p1 in enumerate(points):
            for id2, p2 in enumerate(points):
                pbar.update(1)
                if id1 == id2:
                    continue

                x_min = min(p1[0], p2[0])
                x_max = max(p1[0], p2[0]) + 1
                y_min = min(p1[1], p2[1])
                y_max = max(p1[1], p2[1]) + 1
                # check voor elke mogelijke line of deze door de vierhoek gaat, zo ja, dan is het fout.
                if not a_line_passes_through_square(p1, p2, points):

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
    if test == 24:
        print("Running real input")
        real = run_day("day_9/input.txt")
        print(f"real output: {real}")
