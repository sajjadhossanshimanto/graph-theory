# todo:default dict
'''
things to consider
1. we are not storing inputed edge
2. just ditermining the sortage dis, path is not calculated for now. although it's possible
3. modifing the initial  generated matrix. no copy is saved
4. variable rename u, v, wk= from_node, to_node, selected_node
'''
#%%
from store_graph import graph_input, draw_graph
# from functools import lru_cache


# n=4
inp = '''
1 2 3
2 1 8
1 4 7
4 1 2
2 3 2
3 1 5
3 4 1
'''

graph_input(inp, 1, 1, 1)
draw_graph(0, 1, 1, seed=3083)
# %%
n = -1
# processing input
dis = [[float('inf')]*(n) for _ in range(n)]
for line in inp.split("\n"):
    if not line: continue
    
    u, v, w = map(int, line.split(' '))
    # convert one based indexing to zero
    u-=1
    v-=1
    if max(u, v) > n: n = max(v, u)
    dis[u][v] = w
    dis[u][u] = 0
    dis[v][v] = 0

#%%
# floyd_warshell

for selected_node in range(n):# selecting one
    # now generate row by row
    for row in range(n):
        if row==selected_node:
            # keep as it is
            continue
        
        # generate new values for row
        for coloum in range(n):
            # generating corner of matrix
            if coloum==row: dis[row][coloum] = 0
            elif coloum==selected_node:
                # keep as it is
                continue
            else:
                nd = dis[row][selected_node] + dis[selected_node][coloum]
                if nd<dis[row][coloum]:
                    # TODO: should I consider if its equal? depens actually if i consider connecting multiple edge is better
                    dis[row][coloum] = nd
# %%
