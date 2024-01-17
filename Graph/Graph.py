class Vertex:
    def __init__(self, label):
        self.label = label


class Graph(object):
    def __init__(self):
        self.vertices = []
        self.adjacency_matrix = []

    def has_vertex(self, label):
        return any(vertex.label == label for vertex in self.vertices)

    def get_index(self, label):
        return next((i for i, vertex in enumerate(self.vertices) if vertex.label == label), -1)

    def add_vertex(self, label):
        if not self.has_vertex(label):
            self.vertices.append(Vertex(label))
            self.adjacency_matrix.append([0] * len(self.vertices))
            for row in self.adjacency_matrix:
                row.append(0)

    def add_directed_edge(self, start, finish, weight=1):
        start_index = self.get_index(start)
        finish_index = self.get_index(finish)
        if start_index != -1 and finish_index != -1:
            self.adjacency_matrix[start_index][finish_index] = weight

    def add_undirected_edge(self, start, finish, weight=1):
        start_index = self.get_index(start)
        finish_index = self.get_index(finish)
        if start_index != -1 and finish_index != -1:
            self.adjacency_matrix[start_index][finish_index] = weight
            self.adjacency_matrix[finish_index][start_index] = weight

    def get_edge_weight(self, from_vertex, to_vertex):
        from_index = self.get_index(from_vertex)
        to_index = self.get_index(to_vertex)
        if from_index != -1 and to_index != -1:
            return self.adjacency_matrix[from_index][to_index]
        return -1

    def get_neighbors(self, vertex_label):
        vertex_index = self.get_index(vertex_label)
        if vertex_index != -1:
            return [i for i, weight in enumerate(self.adjacency_matrix[vertex_index]) if weight > 0]
        return []

    def dfs(self, v, visited):
        if v not in visited:
            print(self.vertices[v].label)
            visited.add(v)
            for neighbor in self.get_neighbors(v):
                self.dfs(neighbor, visited)

    def bfs(self, v):
        visited = set()
        queue = [v]

        while queue:
            current_vertex = queue.pop(0)
            if current_vertex not in visited:
                print(self.vertices[current_vertex].label)
                visited.add(current_vertex)
                queue.extend(neigh for neigh in self.get_neighbors(current_vertex) if neigh not in visited)

    def delete_edge(self, from_vertex, to_vertex):
        from_index = self.get_index(from_vertex)
        to_index = self.get_index(to_vertex)
        if from_index != -1 and to_index != -1:
            self.adjacency_matrix[from_index][to_index] = 0
            self.adjacency_matrix[to_index][from_index] = 0

    def delete_vertex(self, vertex_label):
        vertex_index = self.get_index(vertex_label)
        if vertex_index != -1:
            del self.vertices[vertex_index]
            del self.adjacency_matrix[vertex_index]
            for row in self.adjacency_matrix:
                del row[vertex_index]


def main():
    # Test the Graph class

    # Create a graph
    graph = Graph()

    # Add vertices
    for city in ["Houston", "Atlanta", "Kansas City", "Los Angeles", "San Francisco", "Seattle",
                 "Denver", "Chicago", "Boston", "New York", "Dallas", "Miami"]:
        graph.add_vertex(city)

    # Add edges
    graph.add_undirected_edge("Houston", "Atlanta")
    graph.add_undirected_edge("Atlanta", "Kansas City")
    graph.add_undirected_edge("Kansas City", "Chicago")
    graph.add_undirected_edge("Los Angeles", "San Francisco")
    graph.add_undirected_edge("San Francisco", "Seattle")
    graph.add_undirected_edge("Seattle", "Denver")
    graph.add_undirected_edge("Denver", "Chicago")
    graph.add_undirected_edge("Chicago", "Boston")
    graph.add_undirected_edge("Boston", "New York")
    graph.add_undirected_edge("New York", "Dallas")
    graph.add_undirected_edge("Dallas", "Miami")

    # Print Depth First Search
    print("Depth First Search")
    graph.dfs(0, set())  # Assuming starting from the first vertex

    # Print Breadth First Search
    print("\nBreadth First Search")
    graph.bfs(0)  # Assuming starting from the first vertex

    # Delete an edge
    print("\nDeletion of an edge")
    graph.delete_edge("Houston", "Atlanta")

    # Print the adjacency matrix after edge deletion
    print("\nAdjacency Matrix")
    for row in graph.adjacency_matrix:
        print(" ".join(map(str, row)))

    # Delete a vertex
    print("\nDeletion of a vertex")
    graph.delete_vertex("Kansas City")

    # Print the list of vertices and adjacency matrix after vertex deletion
    print("\nList of Vertices")
    for vertex in graph.vertices:
        print(vertex.label)
    print("\nAdjacency Matrix")
    for row in graph.adjacency_matrix:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()


