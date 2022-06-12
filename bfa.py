def bfa(graph, source):
  vertices = graph[0].copy()
  edges = graph[1].copy()
  distances = {key : 999999999 for key in vertices}
  previous = {key : None for key in vertices}
  distances[source] = 0

  for i in range(len(vertices)):
    for edge in edges:
      if distances[edge[0]] + edge[2] < distances[edge[1]]:
        distances[edge[1]] = distances[edge[0]] + edge[2]
        previous[edge[1]] = edge[0]

  for i in range(len(vertices)):
    extra_distances = distances.copy()
    for edge in edges:
        if extra_distances[edge[0]] + edge[2] < extra_distances[edge[1]]:
          extra_distances[edge[1]] = extra_distances[edge[0]] + edge[2]
  
  for vertex in vertices:
    former = distances[vertex]
    current = extra_distances[vertex]
    if current < former:
      distances[vertex] = "-inf"
  return((distances, previous))
