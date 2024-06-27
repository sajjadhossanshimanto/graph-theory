#%%
from store_graph import graph_input, draw_graph


n = 4
inp = '''
1 2 4
1 3 5
3 4 3
4 2 -10
'''
# ans = [inf, 0, -2, 5, 8]

# adj is not required
graph_input(inp, directed=True, weighted=True)
# draw_graph(0, 1, 1)
draw_graph(1, 1, 1, seed = 5643)
#%%
# process input
nodes = []
for line in inp.split('\n'):
    if not line: continue
    nodes.append(list(map(int, line.split(" "))))


#%%
dis = [float("inf")]*(n+1)
def bellman(node):
    dis[node] = 0
    for _ in range(n-1):
        for u, v, w in nodes:
            nd = dis[u]+w
            if nd<dis[v]:
                dis[v] = nd

bellman(1)
# %%
