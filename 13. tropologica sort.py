'''
print dependencies from lift towards right
node having zero out degree sholud be the rightmost node
'''
#%%
from store_graph import graph_input, draw_graph
from collections import deque


n=6
inp = '''
1 2
3 2
4 1
4 3
5 4
6 4
'''

adj = graph_input(inp, directed=True)
draw_graph(directed=True, seed=6291)
# draw_graph(False, True)
#%%
visit = [0]*(n+1)
stack = []
def dfs(node):
    visit[node] = 1
    
    for child in adj[node]:
        if visit[node]: continue
        
        dfs(child)
    
    # print(node, end=" ")
    stack.append(node)

#%%
for node in range(1, n+1):
    if visit[node]: continue
    dfs(node)
print(stack[::-1])
# %%
