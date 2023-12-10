    - do a topological sort in a directed graph


Consider the following graphs - there is one that you could NOT apply the topological sort. Which one is it?
Correct Answer
  there are no vertices where the in-degree is zero 


Topological Sort (Topo Sort)

Works on directed graphs that do not have cycles (DAGs)

0. Determine the in_degree for all vertices. The in_degree is
   the number of edges that are incident on that vertex.

1. Remove the vertices that have an in_degree of 0 to a list and
   remove the out going edges from those vertices. Sort the list
   in a given order. Enqueue the vertices into a Queue and then 
   update the in_degree of all remaining vertices.

2. Repeat step 1 until there are no more vertices in the Graph.

3. Dequeue the vertices and print.


#### **Overview**
A topological sort of a directed, acyclic graph produces a list of the graph's vertices such that for every edge from a vertex X to a vertex Y, X comes before Y in the list.

1. Analysis of each edge in the graph determines if an ordering of vertices is a valid topological sort.
2. If an edge from X to Y exists, X must appear before Y in a valid topological sort. C, D, A, F, B, E is not valid because this requirements is violated for three edges.
3. Ordering D, A, F, E, C, B has 1 edge violating the requirement, so the ordering is not a valid topological sort.
4. For ordering D, A, F, E, B, C, the requirement holds for all edges, so the ordering is a valid topological sort.
5. A graph can have more than 1 valid topological sort. Another valid ordering is D, A, F, B, E, C.


#### **Topological sort algorithm**
The topological sort algorithm uses three lists: a results list that will contain a topological sort of vertices, a no-incoming-edges list of vertices with no incoming edges, and a remaining-edges list. The result list starts as an empty list of vertices. The no-incoming-edges vertex list starts as a list of all vertices in the graph with no incoming edges. The remaining-edges list starts as a list of all edges in the graph.

The algorithm executes while the no-incoming-edges vertex list is not empty. For each iteration, a vertex is removed from the no-incoming-edges list and added to the result list. Next, a temporary list is built by removing all edges in the remaining-edges list that are outgoing from the removed vertex. For each edge currentE in the temporary list, the number of edges in the remaining-edges list that are incoming to currentE's terminating vertex are counted. If the incoming edge count is 0, then currentE's terminating vertex is added to the no-incoming-edges vertex list.

Because each loop iteration can remove any vertex from the no-incoming-edges list, the algorithm's output is not guaranteed to be the graph's only possible topological sort.



GraphTopologicalSort(graph) {
   resultList = empty list of vertices
   noIncoming = list of all vertices with no incoming edges
   remainingEdges = list of all edges in the graph

   while (noIncoming is not empty) {
      currentV = remove any vertex from noIncoming
      Add currentV to resultList
      outgoingEdges = remove currentV's outgoing edges from remainingEdges
      for each edge currentE in outgoingEdges {
         inCount = GraphGetIncomingEdgeCount(remainingEdges, currentE⇢toVertex)
         if (inCount == 0)
            Add currentE⇢toVertex to noIncoming
      }
   }
   return resultList
}


1. The topological sort algorithm begins by initializing an empty result list, a list of all vertices with no incoming edges, and a "remaining edges" list with all edges in the graph.
2. Vertex E is removed from the list of vertices with no incoming edges and added to resultList. Outgoing edges from E are removed from remainingEdges and added to outgoingEdges.
3. Edge EF goes to vertex F, which still has 2 incoming edges. Edge EG goes to vertex G, which still has 1 incoming edge.
4. Vertex A is removed and added to resultList. Outgoing edges from A are removed from remainingEdges. Vertices B and C are added to noIncoming.
5. Vertices C and D are processed, each with 1 outgoing edge.
6. Vertices B and F are processed, each also with 1 outgoing edge.
7. Vertex G is processed last. No outgoing edges remain. The final result is E, A, C, D, B, F, G.