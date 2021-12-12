class Node:
    def __init__(self, value):
        self.value = value
        self.pointers = []

    def get_val(self):
        return self.value

    def get_pointers(self):
        return self.pointers

    def add_pointer(self, node):
        self.pointers.append(node)


class NodeList:
    def __init__(self, list):
        self.nodes = list

    def get_node_by_ref(self, ref):
        n = None
        for node in self.nodes:
            if node.get_val() == ref:
                n = node
        return n

    def get_nodes(self):
        return self.nodes


def init_input():
    f = open('input.txt', 'r')
    return [i.strip() for i in f]


def init_tunnels(inp):
    tunnels = set(inp for tuple in inp for inp in tuple)
    tunnels = [Node(tunnel) for tunnel in tunnels]
    return tunnels


def init_map(inp, tunnels):
    for pair in inp:
        for node in tunnels.get_nodes():
            if pair[0] == node.get_val():
                # Get reference.
                r = tunnels.get_node_by_ref(pair[1])
                node.add_pointer(r)
            if pair[1] == node.get_val():
                r = tunnels.get_node_by_ref(pair[0])
                node.add_pointer(r)

    return tunnels


def find_all_paths(node, lc_visited, revisit, nl):
    now_visited = lc_visited
    if node.get_val() == 'end':
        return 1
    if node in lc_visited:
        if revisit or node.get_val() == 'start':
            return 0
        else:
            revisit = True
    if node.get_val().islower():
        now_visited = lc_visited | {node}
    return sum([find_all_paths(neighbor, now_visited, revisit, nl) for neighbor in nl.get_node_by_ref(node.get_val()).get_pointers()])


def sols():
    inp = [(x.split('-')[0], x.split('-')[1]) for x in init_input()]
    tunnels = NodeList(init_tunnels(inp))

    tunnels = init_map(inp, tunnels)

    start = tunnels.get_node_by_ref('start')

    p_one = find_all_paths(start, set({}), True, tunnels)
    p_two = find_all_paths(start, set({}), False, tunnels)

    return (p_one, p_two)


print(sols())
