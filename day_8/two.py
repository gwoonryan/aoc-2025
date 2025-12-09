from math import sqrt
from itertools import combinations


def point_distance(p1, p2):
    return sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2) + ((p1[2] - p2[2]) ** 2))




def run_day(filename, amount_of_connections) -> int:
    points = []
    connections = []

    with open(filename, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    for line in lines:
        points.append(tuple([int(num) for num in line.split(",")]))

    distances = [(point_distance(p1, p2), p1, p2) for p1, p2 in combinations(points, 2)]
    distances.sort()

    points_to_be_used = points.copy()

    expanded_networks = []
    index = 0
    offset = 0
    # for d in distances:
    #     print(d)
    # quit()
    while True:
        dist, l_p1, l_p2 = distances[index + offset]
        # print(f"p1: {l_p1}, p2: {l_p2}")
        found = False
        for network in expanded_networks:
            if l_p1 in network and l_p2 in network:
                found = True
                break
        if not found:
            connections.append((l_p1, l_p2))
            found_net_ids = []
            if l_p1 in points_to_be_used:
                points_to_be_used.remove(l_p1)
            if l_p2 in points_to_be_used:
                points_to_be_used.remove(l_p2)
            # print("add")
            for id, expanded_network in enumerate(expanded_networks):
                # if found_net_id != -1:
                #   break
                if l_p1 in expanded_network or l_p2 in expanded_network:
                    # if found_net_id != -1 and found_net_id != id:
                    #     print(f"old: {found_net_id}")
                    #     print(f"id: {id}")
                    found_net_ids.append(id)
                    # break
            found_net_ids.sort()
            if len(found_net_ids) == 0:
                expanded_networks.append(set((l_p1, l_p2)))
            elif len(found_net_ids) == 1:
                expanded_networks[found_net_ids[0]].add(l_p1)
                expanded_networks[found_net_ids[0]].add(l_p2)
            elif len(found_net_ids) == 2:
                net_2 = expanded_networks.pop(found_net_ids[1])
                for point in net_2:
                    expanded_networks[found_net_ids[0]].add(point)
                expanded_networks[found_net_ids[0]].add(l_p1)
                expanded_networks[found_net_ids[0]].add(l_p2)
            else:
                assert 1 == 0
        index += 1
        print(index)
        # print(expanded_networks)
        print([len(x) for x in expanded_networks])
        if len(expanded_networks) == 1 and len(points_to_be_used) == 0:
            return l_p1[0] * l_p2[0]

    # expanded_networks.sort(key=lambda x: len(x), reverse=True)
    # print([len(x) for x in expanded_networks])
    # total = 1
    # total *= len(expanded_networks[0])
    # total *= len(expanded_networks[1])
    # total *= len(expanded_networks[2])

    # return total


if __name__ == "__main__":
    # test = run_day("day_8/mytest.txt", 6)
    # print(test)
    # quit()
    # 8800 too low
    test = run_day("day_8/testinput.txt", 10)
    print(f"test output: {test}")
    if test == 25272:
        print("Running real input")
        real = run_day("day_8/input.txt", 1000)
        print(f"real output: {real}")
