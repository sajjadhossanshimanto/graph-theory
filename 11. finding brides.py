'''
new concept: Low time
main purpose of low time is to find whos are connected in the same sub graph
[`yt ref`](https://www.youtube.com/watch?v=64KK9K4RpKE) -> 11:00 min
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
        if child == parent: continue
        if visit[child]:# back edge
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
