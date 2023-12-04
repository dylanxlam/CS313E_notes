determine the minimum spanning tree and give the minimum weight

* Minimum Spanning Tree (MST) - Kruskal's Algorithm and Prim's
  Algorithm.

      * Kruskal's Algorithm
      - Order the edges by increasing weight.
      - Start with an empty graph having only the vertices but no
      edges. Add an edge to this graph as long as it does not form 
      a cycle.
      - When all the vertices are connected you are done.

      * Prim's Algorithm
      - Start with an empty graph having only the vertices.
      - Start with any vertex and add it to the list of visited vertices.
      - Choose the edge with the smallest weight to an unvisited vertex
      as long as it does not form a cycle. Add that vertex to the list
      of visited vertices.
      - Keep adding the edges with the smallest weight from any of the
      vertices in the list of visited vertices as long as those edges
      do not form a cycle.
      - When all the vertices have been visited then you are done.



Consider a graph defined by the following adjacency matrix:

  [[0, 9, 7, 3, 6],

   [9, 0, 8, 4, 5],

   [7, 8, 0, 1, 2],

   [3, 4, 1, 0, 1],

   [6, 5, 2, 1, 0]]

  What is the sum of the weights in the maximum spanning tree?
  27



