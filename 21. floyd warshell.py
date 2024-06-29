# todo: zero based,default dict
#%%
from store_graph import graph_input, draw_graph
# from functools import lru_cache


n=4
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
blank_matrix = [[float('inf')]*(n+1) for _ in range(n+1)]
# processing input
dis = blank_matrix.copy()
for line in inp.split("\n"):
    if not line: continue
    
    u, v, w = map(int, line.split(' '))
    dis[u][v] = w
    dis[u][u] = 0
    dis[v][v] = 0

def floyd_warshell():
    pass

for selected_node in range(1, n+1):# selecting one
    matrix = [[float('inf')*n+1]]
    # now generate row by row
    for row in range(1, n+1):
        if row==selected_node:
            matrix.append(dis[selected_node])
            continue
        
        new_row=[float('inf')]
        for coloum in range(1, n+1):
            # generating corner of matrix
            if coloum==row: row.append(0)
            elif coloum==selected_node:
                new_row.append(dis[row][coloum])
            else:
                nd = dis[row][selected_node] + dis[selected_node][coloum]
                if nd<dis[row][coloum]:
                    # TODO: should is consider if its equal. depens actually if i consider connecting multiple edge is better
                    dis[row][coloum] = nd