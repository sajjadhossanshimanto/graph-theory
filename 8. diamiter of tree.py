#%%
from store_graph import graph_input, draw_graph


n=7
inp = '''
1 2
2 3
2 4
3 7
4 5
4 6
'''
adj_list = graph_input(inp, 7)
draw_graph()

#%%
visit=[0]*(n+1)
max_dis = [0]
root = [-1]
def dfs(node, level=0):
    visit[node]=1
    
    if level>max_dis[0]:
        max_dis[0]=level
        root[0]=node
    for child in adj_list[node]:
        if visit[child]: continue
        
        dfs(child, level+1)

#%%
dfs(1)
print(max_dis[0])
dfs(root[0])
print(max_dis[0])
# %%
