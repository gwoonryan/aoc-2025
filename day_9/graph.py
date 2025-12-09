import matplotlib.pyplot as plt


def read_points(filename):
    points = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines
            # Expect format: x,y
            try:
                x_str, y_str = line.split(',')
                x = float(x_str.strip())
                y = float(y_str.strip())
                points.append((x, y))
            except ValueError:
                print(f"Skipping invalid line: {line!r}")
    return points


def main():
    input_file = "day_9/input.txt"
    points = read_points(input_file)

    if len(points) < 2:
        print("Need at least 2 points to draw lines.")
        return

    # Unpack points into separate lists
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    # Add first point at the end to close the loop (wrap around)
    xs.append(points[0][0])
    ys.append(points[0][1])

    plt.figure()
    # Draw lines connecting the points (including wrap-around)
    plt.plot(xs, ys, marker='o')  # marker='o' to show points as dots

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Points from input.txt with connecting lines")
    plt.axis('equal')  # keep aspect ratio so geometry isn't distorted
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()
