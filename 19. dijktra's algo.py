#%%
from store_graph import graph_input, draw_graph


n = 6
inp = '''
1 2 2
1 3 4
2 4 7
3 5 3
4 5 2
4 6 1
5 6 5
'''

adj = graph_input(inp, n, weighted=True)
# draw_graph(weighted=True, cache=False)
draw_graph(weighted=True, seed=9853)
#%%
sssp = [float("inf")]*(n+1)

def dijksta(node):
    sortest = (node, float('inf'))
    for child, w in adj[node]:
        nd = sssp[node]+w
        if nd<=sssp[child]:
            sssp[child] = nd
            if sssp[child]<sortest[0]:
                sortest =(child, sssp[child])

    if sortest[0]==node: return
    dijksta(sortest[0])

dijksta(1)
# %%
