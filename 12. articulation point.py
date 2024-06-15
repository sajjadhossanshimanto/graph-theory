'''
lower time of child indicates that it has a cycle(alternation edge) connection with ancistor
and removing current edge can not disconnect child from ansistor
so current node cant be a articulation point
'''
#%%
from collections import defaultdict

from store_graph import graph_input, draw_graph


n = 13
inp = '''
1 2
2 4
2 3
3 4
1 5
1 6
5 6
1 7
7 13
7 12
12 13
7 10
7 8
8 10
10 11
8 9
'''

adj = graph_input(inp, n)
draw_graph()
#%%
visit = defaultdict(lambda : 0)
in_time = defaultdict(lambda : 0)
low_time = defaultdict(lambda : 0)

def dfs(node, parent, timer=1):
    visit[node] = 1
    in_time[node] = timer
    low_time[node] = timer
    for child in adj[node]:
        if child == parent: continue
        if visit:# back edge
#                                in_time[child] # what should i do
            low_time[node] = min(low_time[child], low_time[node])
        else:
            timer+=1
            dfs(child, node, timer)
            # if in_time[node]>low_time[child]:
            #     # no back connection
            if not in_time[node]>low_time[child]:# articulation point
                low_time[node] = min(low_time[node], low_time[child])
                print(f"articulation point {node}")
#%%














