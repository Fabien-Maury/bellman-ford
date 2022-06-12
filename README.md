# Bellman-Ford algorithm
Python3 implementation of Bellman-Ford algorithm for shortest path in negative-weighted graphs

* Input : 
  graph : a tuple containing vertices, a list of vertices; and edges, a list of edges written as : (vertex1, vertex2, weight)
  source : the vertex used as soiurce for the pathes
  
* Output : 
  a tuple containing : 
    - a dictionnary of the shortest distance to each vertex
    - a dictionnary of the previous vertex used in the path to each vertex shortest distance
