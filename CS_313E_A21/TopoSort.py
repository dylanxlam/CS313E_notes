#  File: TopoSort.py

#  Description: This code implements a topological sort 
#  for a directed graph, checking for cycles using Depth-First 
#  Search (DFS) and then performing a topological sort if no 
#  cycle is detected. The graph manipulation includes adding 
#  directed edges and obtaining immediate neighbors.

#  Student Name: Alexander Romero-Barrionuevo

#  Student UT EID: ANR3784

#  Partner Name: Dylan Lam

#  Partner UT EID: DXL85

#  Course Name: CS 313E

#  Unique Number: 52605

#  Date Created: 12/3/2023

#  Date Last Modified: 12/3/2023

import sys

class Stack(object):
	def __init__(self):
		self.stack = []

	# add an item to the top of the stack
	def push(self, item):
		self.stack.append(item)

	# remove an item from the top of the stack
	def pop(self):
		return self.stack.pop()

	# check the item on the top of the stack
	def peek(self):
		return self.stack[-1]

	# check if the stack if empty
	def is_empty(self):
		return len(self.stack) == 0

	# return the number of elements in the stack
	def size(self):
		return len(self.stack)


class Queue(object):
	def __init__(self):
		self.queue = []

	# add an item to the end of the queue
	def enqueue(self, item):
		self.queue.append(item)

	# remove an item from the beginning of the queue
	def dequeue(self):
		return self.queue.pop(0)

	# check if the queue is empty
	def is_empty(self):
		return len(self.queue) == 0

	# return the size of the queue
	def size(self):
		return len(self.queue)

class Vertex(object):
	def __init__(self, label):
		self.label = label
		self.visited = False

	# determine if a vertex was visited
	def was_visited(self):
		return self.visited

	# determine the label of the vertex
	def get_label(self):
		return self.label

	# string representation of the vertex
	def __str__(self):
		return str(self.label)


class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        for vertex in self.Vertices:
            if vertex.get_label() == label:
                return True
        return False

    # get the index from the vertex label
    def get_index(self, label):
        for i, vertex in enumerate(self.Vertices):
            if vertex.get_label() == label:
                return i
        return -1

    # add a Vertex object with a given label to the graph
    def add_vertex(self, label):
        if not self.has_vertex(label):
            self.Vertices.append(Vertex(label))
            for row in self.adjMat:
                row.append(0)
            self.adjMat.append([0] * len(self.Vertices))

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        start_index = self.get_index(start)
        finish_index = self.get_index(finish)

        if start_index != -1 and finish_index != -1:
            self.adjMat[start_index][finish_index] = weight

    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle(self):
        stack = Stack()
        visited = [False] * len(self.Vertices)

        for i in range(len(self.Vertices)):
            if not visited[i]:
                if self.has_cycle_util(i, visited, stack):
                    return True

        return False

    # Helper method to check for a cycle in a directed graph using DFS.
    def has_cycle_util(self, v, visited, stack):
        visited[v] = True
        stack.push(v)

        for neighbor in self.get_neighbors(self.Vertices[v].get_label()):
            neighbor_index = self.get_index(neighbor)
            if not visited[neighbor_index]:
                if self.has_cycle_util(neighbor_index, visited, stack):
                    return True
            elif neighbor_index in stack.stack:
                return True

        stack.pop()
        return False

    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort(self):
        if self.has_cycle():
            return None

        stack = Stack()
        visited = [False] * len(self.Vertices)

        for i in range(len(self.Vertices)):
            if not visited[i]:
                self.toposort_util(i, visited, stack)

        result = []
        while not stack.is_empty():
            result.append(self.Vertices[stack.pop()].get_label())

        return result

    # Utility function to perform topological sort using DFS.
    def toposort_util(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.get_neighbors(self.Vertices[v].get_label()):
            neighbor_index = self.get_index(neighbor)
            if not visited[neighbor_index]:
                self.toposort_util(neighbor_index, visited, stack)

        stack.push(v)

    # get a list of immediate neighbors that you can go to from a vertex
    # return a list of indices or an empty list if there are none
    def get_neighbors(self, vertexLabel):
        neighbors = []
        v_index = self.get_index(vertexLabel)
        for i in range(len(self.Vertices)):
            if self.adjMat[v_index][i] != 0:
                neighbors.append(self.Vertices[i].get_label())
        return neighbors

def main():
    # create the Graph object
    theGraph = Graph()

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    num_vertices = int(line)

    # read the vertices to the list of Vertices
    for i in range(num_vertices):
        line = sys.stdin.readline()
        city = line.strip()
        theGraph.add_vertex(city)

    # read the number of edges
    line = sys.stdin.readline()
    line = line.strip()
    num_edges = int(line)

    # read each edge and place it in the adjacency matrix
    for i in range(num_edges):
        line = sys.stdin.readline()
        edge = line.strip().split()

        # Check if the edge list is not empty
        if len(edge) >= 2:
            start = edge[0]
            finish = edge[1] if len(edge) > 1 else None
            weight = int(edge[2]) if len(edge) == 3 else 1

            theGraph.add_directed_edge(start, finish, weight)

    # print whether the graph has a cycle or not
    if theGraph.has_cycle():
        print("The Graph has a cycle.")
    else:
        print("The Graph does not have a cycle.")

    # print the list of vertices after toposort
    print("\nList of vertices after toposort")
    vertex_list = theGraph.toposort()
    print(vertex_list)

if __name__ == "__main__":
    main()