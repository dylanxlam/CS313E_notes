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