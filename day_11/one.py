import queue
import tqdm


def run_day(filename) -> int:
    problems = []
    total = 0

    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    for line in lines:
        split = line.split(" ")
        problems.append((split[0][:-1], split[1:]))

    graph = {node: paths for node, paths in problems}  # node -> next nodes

    # lengths = {}

    # parents = {}  # node -> backward

    Q = queue.Queue()
    Q.put("you")
    total = 0
    while Q.qsize() > 0:
        v = Q.get()
        # print(v)
        if v == "out":
            # length = lengths[v] + 1
            # print(length)
            total += 1
        else:
            for next in graph[v]:
                # parents[next] = v
                # lengths[next] = lengths[v] + 1
                Q.put(next)
    return total

    return total


if __name__ == "__main__":

    test = run_day("day_11/testinput.txt")
    print(f"test output: {test}")
    if test == 5:
        print("Running real input")
        real = run_day("day_11/input.txt")
        print(f"real output: {real}")
