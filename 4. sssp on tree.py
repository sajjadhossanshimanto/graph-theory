# single source sortest path
#%%
from store_graph import graph_input, draw_graph
from collections import deque


n=6

inp = '''
1 2
1 3
1 4
2 5
2 6
'''
adj_list = graph_input(inp, n)

#%%
visit = [0]*(n+1)
dis = [0]*(n+1)
def bfs(root):
    level = 0
    queue = deque([root])
    while queue:
        node = queue.popleft()
        for child in adj_list[node]:
            if visit[child]: continue
            visit[child] = 1
            dis[child] = level+1
            queue.append(child)
        level+=1

#%%
src = 1
bfs(src)


# %%
dis[5]