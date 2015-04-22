class Cant_follow_yourself(Exception):
    pass


class Already_there(Exception):
    pass


class DirectedGraph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node in self.nodes:
            raise Already_there
        self.nodes.update({node: set()})

    def add_edge(self, node1, node2):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)
        if node1 == node2:
            raise Cant_follow_yourself
        self.nodes[node1].add(node2)

    def get_neighbours(self, node):
        return self.nodes[node]

    def bfs(self, node1):
        visited = set()
        queue = []
        queue.append(node1)
        visited.add(node1)
        while len(queue) != 0:
            current_node = queue.pop(0)
            for pointed_node in self.nodes[current_node]:
                if pointed_node not in visited:
                    queue.append(pointed_node)
                    visited.add(pointed_node)
        return visited

    def path_between(self, node1, node2):
        connected_to_node = self.bfs(node1)
        if node2 in connected_to_node:
            return True
        else:
            return False

    def edge_between(self, node1, node2):
        return node2 in self.nodes[node1]
