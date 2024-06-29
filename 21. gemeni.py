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

# ... (rest of your code for processing input and printing results)
