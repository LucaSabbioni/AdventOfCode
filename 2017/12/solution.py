

def find_len(node: int, singletons: list[int], connected_components: list[set[int]]):
    if node in set(singletons):
        return 1
    for component in connected_components:
        if node in component:
            return len(component)


def read_file(path):
    connected_components = []
    singletons = []
    with open(path) as file:
        for line in file:
            node, neighbors = line.split(' <-> ')
            neighbors_set = set(map(int, neighbors.split(', ')))
            connections = set([int(node)]).union(neighbors_set)
            new_connected_component = connections
            # excluding singleton nodes
            if len(new_connected_component)==1:
                singletons.append(node)
            else:
                for component in connected_components:
                    if len(connections.intersection(component)) > 0:
                        new_connected_component = new_connected_component.union(component)
                        connected_components.remove(component)

                connected_components.append(new_connected_component)
    return singletons, connected_components


if __name__ == '__main__':
    path = 'input.txt'
    singletons, connected_components = read_file(path)
    solution1 = find_len(0, singletons, connected_components)
    print('Part 1: ', solution1)
    solution2 = len(singletons) + len(connected_components)
    print('Part 2: ', solution2)
