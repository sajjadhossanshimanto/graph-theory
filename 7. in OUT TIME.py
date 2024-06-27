'''
## Motivation
given 2 nodes find whether one nodes lies in sub tree of other node
'''
#%%
from store_graph import graph_input, draw_graph


n=7
inp = '''
1 2
2 3
2 4
3 5
4 6
4 7
'''

n=5
inp='''
1 2
2 3
2 4
4 5
'''


adj_list = graph_input(inp)
draw_graph()
#%%
visit = [0]*(n+1)
in_time = [0]*(n+1)
out_time = [0]*(n+1)
def dfs(node, timer=1):
    visit[node] = 1
    in_time[node] = timer
    
    for child in adj_list[node]:
        if visit[child]: continue
        
        timer = dfs(child, timer+1)
        timer+=1
    
    out_time[node] = timer
    return timer

dfs(1)
#%%
# if b lies in the subtree of a
a, b = map(int, input().split(" "))
if  out_time[a]>in_time[b]>in_time[a]:
    print("yes")
else:
    print("no")
    
# %%
