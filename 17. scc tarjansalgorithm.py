#%%
from store_graph import graph_input, draw_graph


n=6
inp = '''
0 1
1 0
2 1
2 0
2 3
3 2
4 1
4 3
4 5
5 3
5 6
6 4
'''
adj = graph_input(inp, n, strong_edge=True)

# draw_graph(cache=False, strong_edge=True)
draw_graph(strong_edge=True, seed=9077)
#%%
in_time = [-1]*(n+1)
low_time = [-1]*(n+1)
on_stack=[False]*(n+1)# True False
stack = []
cc=[0]# counter
def dfs(node, timer=1):
    stack.append(node)
    on_stack[node] = 1
    low_time[node] = timer
    in_time[node] = timer
    
    for child in adj[node]:
        # if visit[child]: continue# not gonna work here. 
        # cause evenif 1 is child of 0 and 
        # 0 is visited previously we need to lower the value of 1
        if in_time[node]==-1:# same as #if not visited:
            timer+=1
            dfs(child, timer)
        if on_stack[child]:# doesn't matter even if visited
            low_time[node] = min(low_time[node], low_time[child])# maigic hapens here
    
    if low_time[node]==in_time[node]:# then is't not a part of cycle or root of cycle
        # empty until all childs are removed
        while True: # do while loop  simulation
            child = stack.pop()
            if node==child: break
            on_stack[child] = False
            low_time[child] = low_time[node]# smart move for the iddue of dfs oder
        cc[0]+=1

# %%
dfs(0)
print(cc[0])
# %%
