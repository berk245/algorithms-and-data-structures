class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.graph_dictionary = {}
        for start, end in edges:
            if start not in self.graph_dictionary:
                self.graph_dictionary[start] = {end}
            else:
                self.graph_dictionary[start].add(end)

    def add_node(self, node):
        if node in self.graph_dictionary:
            return

        self.graph_dictionary[node] = None

    def add_edge(self, edge):
        if edge[0] not in self.graph_dictionary:
            return
        self.graph_dictionary[edge[0]].add(edge[1])

    def remove_node(self, node_to_del):
        self.graph_dictionary.pop(node_to_del, None)

        for node in self.graph_dictionary:
            if node_to_del in self.graph_dictionary[node]:
                self.graph_dictionary[node].remove(node_to_del)

        return

    def remove_edge(self, edge):
        if edge[0] in self.graph_dictionary:
            try:
                self.graph_dictionary[edge[0]].remove(edge[1])
            except:
                return

    def geth_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dictionary:
            return []
        paths = []
        for next_stop in self.graph_dictionary[start]:
            # check if this node has already been visited
            if next_stop not in path:
                new_paths = self.geth_paths(next_stop, end, path)

                for p in new_paths:
                    paths.append(p)
        return paths


tups = [['Paris', 'Barcelona'], ['Paris', 'Amsterdam'], ['Barcelona',
                                                         'Amsterdam'], ['Amsterdam', 'Madrid'], ['Barcelona',
                                                                                                 'Amsterdam'], ['Barcelona', 'Madrid'], ['Madrid', 'London']]

G = Graph(tups)

print(G.graph_dictionary)

print(G.geth_paths('Paris', 'London'))
