#%%
from store_graph import graph_input, draw_graph
from heapq import heappop, heappush


n = 6
inp = '''
1 2 2
1 3 4
2 3 1
2 4 7
3 5 3
4 5 2
4 6 1
5 6 5
'''
# ans: [inf, 0, 2, 3, 8, 6, 9]

adj = graph_input(inp, weighted=True)
# draw_graph(weighted=True, cache=False)
draw_graph(weighted=True, seed=5756)
#%%
sssp = [float("inf")]*(n+1)

def dijksta(node):
    sssp[node]=0# make sure starting node has dis 0

    pq = []
    heappush(pq, (0, node))
    while pq:
        dis, node = heappop(pq)
        # if node in visit: continue# a node might get visited multiple time
        if dis>sssp[node]: continue
        for child, w in adj[node]:
            nd = dis+w
            if nd>sssp[child]: continue
            sssp[child] = nd
            heappush(pq, (nd, child))
    return

dijksta(1)
# %%
