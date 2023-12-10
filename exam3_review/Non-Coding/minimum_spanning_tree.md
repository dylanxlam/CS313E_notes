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


#### **Overview**
A graph's minimum spanning tree is a subset of the graph's edges that connect all vertices in the graph together with the minimum sum of edge weights. The graph must be weighted and connected. A connected graph contains a path between every pair of vertices.


1. A minimum spanning tree can be used to find the minimal amount of power lines needed to connect cities. Each vertex represents a city. Edges represent roads between cities. The city P has a power plant.
2. Power lines are along roads, such that each city is connected to a powered city. But power lines along every road would be excessive.
3. The minimum spanning tree, shown in red, is the set of edges that connect all cities to power with minimal total power line length.
4. The resulting minimum spanning tree can be viewed as a tree with the power plant city as the root.

#### **Kruskal's minimum spanning tree algorithm**
Kruskal's minimum spanning tree algorithm determines subset of the graph's edges that connect all vertices in an undirected graph with the minimum sum of edge weights. Kruskal's minimum spanning tree algorithm uses 3 collections:

An edge list initialized with all edges in the graph.
A collection of vertex sets that represent the subsets of vertices connected by current set of edges in the minimum spanning tree. Initially, the vertex sets consists of one set for each vertex.
A set of edges forming the resulting minimum spanning tree.
The algorithm executes while the collection of vertex sets has at least 2 sets and the edge list has at least 1 edge. In each iteration, the edge with the lowest weight is removed from the list of edges. If the removed edge connects two different vertex sets, then the edge is added to the resulting minimum spanning tree, and the two vertex sets are merged.



KruskalsMinimumSpanningTree(graph) {
   edgeList = list containing all edges from graph
   vertexSets = collection of vertex sets, empty initially
   for each vertex V in graph
      Add new set containing only V to vertexSets
   resultList = new, empty set of edges

   while (vertexSets⇢length > 1 && edgeList⇢length > 0) {
      nextEdge = remove edge with minimum weight from edgeList
      vSet1 = set in vertexSets containing nextEdge⇢vertex1
      vSet2 = set in vertexSets containing nextEdge⇢vertex2
      if (vSet1 != vSet2) {
         Add nextEdge to resultList
         Remove vSet1 and vSet2 from vertexSets
         merged = union(vSet1, vSet2)
         Add merged to vertexSets
      }
   }
   return resultList
}


1. An edge list, a collection of vertex sets, and an empty result set are initialized. The edge list contains all edges from the graph.
2. Edge AD is removed from the edge list and added to resultList, which will contain the edges forming the minimum spanning tree.
3. The next 5 edges connect different vertex sets and are added to the result.
4. Edges AB and CE both connect 2 vertices that are in the same vertex set, and therefore are not added to the result.
5. Edge EF connects the 2 remaining vertex sets.
6. One vertex set remains, so the minimum spanning tree is complete.