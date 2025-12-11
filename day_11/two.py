import graphviz
import queue
import tqdm
from functools import cache

# def find_num_paths_from_x_to_y(x, y, excluded_nodes, graph):
#     Q = queue.Queue()
#     Q.put(x)
#     total = 0
#     while Q.qsize() > 0:
#         v = Q.get()
#         print(Q.qsize())
#         if v == y:
#             # length = lengths[v] + 1
#             # print(length)
#             total += 1
#         elif v in excluded_nodes:
#             pass
#         else:
#             for next in graph[v]:
#                 # parents[next] = v
#                 # lengths[next] = lengths[v] + 1
#                 Q.put(next)
#     return total





def run_day(filename) -> int:
    # dot = graphviz.Digraph(comment='The Round Table')
    problems = []
    total = 0

    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    for line in lines:
        split = line.split(" ")
        problems.append((split[0][:-1], split[1:]))

    graph = {node: paths for node, paths in problems}  # node -> next nodes

    # for key in graph.keys():
    #     if key == "dac" or key == "fft":
    #         dot.node(key, shape="star")
    #     else:
    #         dot.node(key)

    # for key, val in graph.items():
    #     for edge in val:
    #         dot.edge(key, edge)

    # dot.render('doctest-output/round-table.gv', view=True)
    # quit()

    # total_srv_to_fft = 4436

    # total_srv_to_fft = find_num_paths_from_x_to_y("svr", "fft", set(["qbe", "aww", "oln", "els", "stn"]), graph)
    # print(total_srv_to_fft)
    # quit()

    # Q = queue.Queue()
    # Q.put("fft")
    # excluded = set(["cmj", "you", "ufz", "mqo"])
    # total_fft_to_dac = 0
    # while Q.qsize() > 0:
    #     print(Q.qsize())
    #     v = Q.get()
    #     # print(v)
    #     if v == "dac":
    #         # length = lengths[v] + 1
    #         # print(length)
    #         total_fft_to_dac += 1
    #     elif v == "out" or v in excluded:
    #         pass
    #     else:
    #         for next in graph[v]:
    #             # parents[next] = v
    #             # lengths[next] = lengths[v] + 1
    #             Q.put(next)

    # Q = queue.Queue()
    # Q.put("dac")
    # total_dac_to_end = 0
    # while Q.qsize() > 0:
    #     print(Q.qsize())
    #     v = Q.get()
    #     # print(v)
    #     if v == "out":
    #         # length = lengths[v] + 1
    #         # print(length)
    #         total_dac_to_end += 1
    #     else:
    #         for next in graph[v]:
    #             # parents[next] = v
    #             # lengths[next] = lengths[v] + 1
    #             Q.put(next)

    # print(f"srv_to_fft {total_svr_to_fft}")
    # print(f"fft_to_dac {total_fft_to_dac}")
    # print(f"dac_to_end {total_dac_to_end}")
    # print(" ")

    @cache
    def np(v, d, f):
        if v == 'out':
            return 1 if d and f else 0
        return sum(np(w, d if d else v == 'dac', f if f else v == 'fft') for w in graph[v])

    return np("svr", False, False)


if __name__ == "__main__":

    test = run_day("day_11/testinput.txt")
    print(f"test output: {test}")
    if test == 2:
        print("Running real input")
        real = run_day("day_11/input.txt")
        print(f"real output: {real}")
