#%%
from store_graph import graph_input, draw_graph


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
    sortest = (node, float('inf'))
    for child, w in adj[node]:
        nd = sssp[node]+w
        if nd<=sssp[child]:
            sssp[child] = nd
            if sssp[child]<sortest[1]:
                sortest =(child, sssp[child])

    if sortest[0]==node: return
    dijksta(sortest[0])

sssp[1]=0# make sure starting node has dis 0
dijksta(1)
# %%
