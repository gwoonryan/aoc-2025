import pulp
import tqdm


def solve_problem(lights, buttons, joltage_str) -> int:
    joltage = [int(x) for x in joltage_str[1:-1].split(",")]
    n_joltage = len(joltage)

    prob = pulp.LpProblem("current_problem", pulp.LpMinimize)
    index_problems = {x: [] for x in range(n_joltage)}

    button_vars = {}

    for id, str_button in enumerate(buttons):
        button_var = pulp.LpVariable(f"button_{id}", 0, max(joltage), cat="Integer")
        button_vars[id] = button_var
        button_indexes = [int(x) for x in str_button[1:-1].split(",")]
        for index in button_indexes:
            index_problems[index].append(button_var)

    for key, value in index_problems.items():
        prob += (pulp.lpSum(value) == joltage[key])
    prob += pulp.lpSum(button_vars.values())

    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    button_values = [pulp.value(var) for var in button_vars.values()]

    return sum(button_values)


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
        # for problem in problems:
        out = solve_problem(*problem)
        assert out != -1
        total += out

    return total


if __name__ == "__main__":
    # 18945 low
    test = run_day("day_10/testinput.txt")
    print(f"test output: {test}")
    if test == 33:
        print("Running real input")
        real = run_day("day_10/input.txt")
        print(f"real output: {real}")
