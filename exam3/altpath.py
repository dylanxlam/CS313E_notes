class Graph:
    def __init__(self):
        # list %vertices% stores labels of all vertices in graph
        # matrix %adjmat% stores adjacency matrix of the graph
        self.vertices = []
        self.adjmat = []

    # add a vertex with given label
    def add_vertex(self, label):
        self.vertices.append(label)
        for i in range(len(self.vertices) - 1):
            self.adjmat[i].append(0)
        row = []
        for _ in range(len(self.vertices)):
            row.append(0)
        self.adjmat.append(row)

    # get the vertex index for a given label
    def get_index(self, label):
        return self.vertices.index(label)


    # add an undirected edge between vertices v1 and v2 with given weight
    def add_edge(self, v1, v2, weight):
        p, q = self.get_index(v1), self.get_index(v2)
        self.adjmat[p][q] = self.adjmat[q][p] = weight

    # You need to implement this function that returns True if and only if there exists a path from v1 to v2 with given length
    # Note that v1, v2 here are labels, NOT indeices
    def search(self, v1, v2, length):
        index_v1, index_v2 = self.get_index(v1), self.get_index(v2)
        visited = set()

        def dfs(current, current_length):
            if current == index_v2 and current_length == length:
                return True
            visited.add(current)

            for neighbor, weight in enumerate(self.adjmat[current]):
                if weight > 0 and neighbor not in visited:
                    if dfs(neighbor, current_length + weight):
                        return True

            visited.remove(current)
            return False

        return dfs(index_v1, 0)

def main():
    # The following is an example
    g = Graph()
    g.add_vertex('n1')
    g.add_vertex('n2')
    g.add_vertex('n3')
    g.add_vertex('n4')
    g.add_vertex('n5')
    g.add_edge('n1', 'n2', 1)
    g.add_edge('n2', 'n3', 5)
    g.add_edge('n3', 'n4', 3)
    g.add_edge('n3', 'n5', 9)
    g.add_edge('n1', 'n5', 4)

    print(f'Find the path from n1 to n2 with length 2. Expected answer: False, your answer: {g.search("n1", "n2", 2)}')
    print(f'Find the path from n1 to n2 with length 20. Expected answer: True, your answer: {g.search("n1", "n2", 18)}')
    print(f'Find the path from n3 to n5 with length 10. Expected answer: True, your answer: {g.search("n3", "n5", 10)}')

if __name__ == '__main__':
    main()
