from math import sqrt
from itertools import combinations


def point_distance(p1, p2):
    return sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2) + ((p1[2] - p2[2]) ** 2))


def get_expanded_networks(connections):
    expanded_networks = []
    for connection in connections:
        found_net_ids = []
        for id, expanded_network in enumerate(expanded_networks):
            # if found_net_id != -1:
            #   break
            if connection[0] in expanded_network or connection[1] in expanded_network:
                # if found_net_id != -1 and found_net_id != id:
                #     print(f"old: {found_net_id}")
                #     print(f"id: {id}")
                found_net_ids.append(id)
                # break
        found_net_ids.sort()
        if len(found_net_ids) == 0:
            expanded_networks.append(set([connection[0], connection[1]]))
        elif len(found_net_ids) == 1:
            expanded_networks[found_net_ids[0]].add(connection[0])
            expanded_networks[found_net_ids[0]].add(connection[1])
        elif len(found_net_ids) == 2:
            net_2 = expanded_networks.pop(found_net_ids[1])
            for point in net_2:
                expanded_networks[found_net_ids[0]].add(point)
            expanded_networks[found_net_ids[0]].add(connection[0])
            expanded_networks[found_net_ids[0]].add(connection[1])
        else:
            assert 1 == 0

    # networks = []
    # for connection in connections:
    #     found_net_id = -1
    #     for id, network in enumerate(networks):
    #         # if found_net_id != -1:
    #         #     break
    #         for net_con in network:
    #             if connection[0] in net_con or connection[1] in net_con:
    #                 found_net_id = id
    #                 # break
    #     if found_net_id == -1:
    #         networks.append([connection])
    #     else:
    #         networks[found_net_id].append(connection)

    # expanded_networks = []

    # for network in networks:
    #     expanded_networks.append(set())
    #     for net_con in network:
    #         expanded_networks[-1].add(net_con[0])
    #         expanded_networks[-1].add(net_con[1])
    return expanded_networks


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

    expanded_networks = []
    index = 0
    offset = 0
    # for d in distances:
    #     print(d)
    # quit()
    while index < amount_of_connections - 1:
        dist, l_p1, l_p2 = distances[index + offset]
        # print(f"p1: {l_p1}, p2: {l_p2}")
        expanded_networks = get_expanded_networks(connections)
        found = False
        for network in expanded_networks:
            if l_p1 in network and l_p2 in network:
                found = True
                break
        # print(f"{l_p1}, {l_p2}")
        if not found:
            # print("add")
            connections.append((l_p1, l_p2))
            index += 1
        else:
            # print("illegal!")
            offset += 1
        print(index)
        expanded_networks = get_expanded_networks(connections)
        # print(expanded_networks)
        # print([len(x) for x in expanded_networks])

    expanded_networks = get_expanded_networks(connections)

    expanded_networks.sort(key=lambda x: len(x), reverse=True)
    print([len(x) for x in expanded_networks])
    total = 1
    total *= len(expanded_networks[0])
    total *= len(expanded_networks[1])
    total *= len(expanded_networks[2])

    return total


if __name__ == "__main__":
    # test = run_day("day_8/mytest.txt", 6)
    # print(test)
    # quit()
    # 8800 too low
    test = run_day("day_8/testinput.txt", 10)
    print(f"test output: {test}")
    if test == 40:
        print("Running real input")
        real = run_day("day_8/input.txt", 1000)
        print(f"real output: {real}")
