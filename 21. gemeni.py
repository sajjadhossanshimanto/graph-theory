def floyd_warshall(edges):
  """
  Finds the shortest paths between all pairs of nodes in a weighted graph.

  Args:
    edges: A list of tuples representing edges (source, destination, weight).

  Returns:
    A list of lists containing the shortest distances between all pairs of nodes.
  """

  n = max(u + 1 for u, _, _ in edges)  # Number of nodes based on max vertex index

  # Initialize distances with infinity (except for diagonals)
  dist = [[float('inf')] * n for _ in range(n)]
  for i in range(n):
    dist[i][i] = 0

  # Fill in known edge weights
  for u, v, w in edges:
    dist[u][v] = w

  # Floyd-Warshall algorithm (separate loops)
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][k] + dist[k][j] < dist[i][j]:
          dist[i][j] = dist[i][k] + dist[k][j]

  return dist


# Processing input (assuming weights are space-separated integers in each line)
inp = """
1 2 3
2 1 8
1 4 7
4 1 2
2 3 2
3 1 5
3 4 1
"""

edges = []
for line in inp.splitlines():
  if not line:
    continue
  u, v, w = map(int, line.split())
  edges.append((u - 1, v - 1, w))

# Floyd-Warshall
shortest_distances = floyd_warshall(edges.copy())  # Copy to avoid modifying input

print(shortest_distances)