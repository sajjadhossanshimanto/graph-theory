'''
## Observation
1. tree is a one single connected component
2. there is no cycle
3. for tree if there are n nodes have n-1 edge
'''
#%%
from store_graph import graph_input, draw_graph


n=4
m=3
inp = '''
1 2
2 3
2 4
'''
adj_list = graph_input(inp)

#%%
visit = [0]*(n+1)
def dfs(node):
    visit[node]=1
    for child in adj_list[node]:
        if not visit[child]: dfs(child)

#%%
if m!=(n-1):# that also verifies backedge
    print("NO1")
else:
    cc=0
    for i in range(1, n+1):# error ocure for rage(0,  n)
        if visit[i]: continue
        
        dfs(i)
        cc+=1
    
    if cc==1: print("yes")
    else: print("NO2")

# %%
