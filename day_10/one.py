import queue
import tqdm


def solve_problem(lights, buttons, joltage) -> int:
    # construct graph
    amount_of_lights = len(lights) - 2
    amount_of_nodes = 2**amount_of_lights
    end = lights[1:-1]

    graph = {}  # node -> next nodes
    lengths = {}  # node -> distance
    first = None

    for node in range(amount_of_nodes):
        bits = format(node, 'b')
        bits = bits.zfill(amount_of_lights)
        string = bits.translate(str.maketrans('01', '.#'))
        graph[string] = set()
        lengths[string] = -1
        if first is None:
            first = string
        for str_button in buttons:
            button = [int(x) for x in str_button[1:-1].split(",")]
            new_node = [chr for chr in string]
            for num in button:
                old = new_node[num]
                if old == "#":
                    new_node[num] = "."
                else:
                    new_node[num] = "#"
            st = "".join(new_node)
            graph[string].add(st)

    # print(graph)

    # apply dfs
    parents = {}  # node -> backward
    explored = set([first])

    Q = queue.Queue()
    Q.put(first)

    while Q.qsize() > 0:
        v = Q.get()
        # print(v)
        if v == end:
            length = lengths[v] + 1
            # print(length)
            return length
        for next in graph[v]:
            if next not in explored:
                explored.add(next)
                parents[next] = v
                lengths[next] = lengths[v] + 1
                Q.put(next)
    return -1


def run_day(filename) -> int:
    problems = []
    total = 0

    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    for line in lines:
        split = line.split(" ")
        problems.append((split[0], tuple(split[1:-1]), split[-1]))

    for problem in tqdm.tqdm(problems):
        out = solve_problem(*problem)
        assert out != -1
        total += out

    return total


if __name__ == "__main__":

    test = run_day("day_10/testinput.txt")
    print(f"test output: {test}")
    if test == 7:
        print("Running real input")
        real = run_day("day_10/input.txt")
        print(f"real output: {real}")
