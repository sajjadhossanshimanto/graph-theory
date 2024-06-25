'''
learned from https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
'''
#%%
from store_graph import graph_input, draw_graph
import heapq


n = 8
inp = '''
7 6 1
8 2 2
6 5 2
0 1 4
2 5 4
8 6 6
2 3 7
7 8 7
0 7 8
1 2 8
3 4 9
5 4 10
1 7 11
3 5 14
'''
adj = graph_input(inp, n, weighted=True)
draw_graph(0, weighted=True)

#%%
# 1st take the lowest edge
edge_q = [(0, 0)]# (0, 0) taken as dump edge. its better than finding min among weights

res = 0
visit = [0]*(n+1)
while edge_q:
    u, w = heapq.heappop(edge_q)
    if visit[u]: continue# yes primmes algo works with nodes

    visit[u]=1
    res += w
    
    # main thisng here
    for v, w in adj[u]:
        if visit[v]: continue
        heapq.heappush(edge_q, (v, w))

print(res)