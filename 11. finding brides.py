'''
new concept: Low time
'''
#%%
from store_graph import graph_input, draw_graph


n=4
inp = '''
1 2
2 3
2 4
3 4
'''

adj = graph_input(inp, n)

#%%
visit = [0]*(n+1)
in_time = [0]*(n+1)
low_time = [0]*(n+1)
def dfs(node, parent, time=1):
    visit[node]=1
    in_time[node] = time
    low_time[node] = time
    
    for child in adj[node]:
        # 3 posibilities 
        if visit[child]:
            if child == parent: continue
            else: # back edge
                low_time[node] = min(low_time[node], in_time[child])
        else:# normal edge
            time+=1
            dfs(child, node, time)
            if low_time[child]<=low_time[node]:
                # backtracked from back edge
                low_time[node]=low_time[child]
            else:
                print(f"bridge directed {node}--{child}")

#%%
dfs(1, -1)

# %%
