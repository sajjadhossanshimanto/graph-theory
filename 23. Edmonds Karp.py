#%%
'''
1. memory can be reduced: by avoiding `capacity matrix`. 
- use weigght system. maynot be possible actually. even if i want to caltulat residual capacity one the go i need the base capacity

# learnoing 
- we use `weight matrix` when we need both direct and reverse edge
'''

#%%
from collections import deque, defaultdict


#%%
def bfs(s, t):
    n = len(capacity)
    parent = [-1]*n# need for backtracking
    
    q = deque([(s, float("inf"))])# [(node, flow), ....]
    while not q.empty():
        node, flow = q.popleft()
        
        for child in adj[node]:
            if parent[child]==-1 and capacity[node][child]:
                parent[child] = node
                new_flow = min(flow, capacity[node][chld])
                
                if child==t: return new_flow, parent
                q.append((child, new_flow))

#%%
def max_flow(s, t):
    flow = 0
    
    new_flow = True
    while new_flow:# as long as no more flow available
        new_flow, parent = bfs(s, t)
        flow+=new_flow
        
        # back tracking
        cur = t
        while cur!=s:
            prev = parent[cur]
            capacity[prev][cur] -= new_flow# direct edge
            capacity[cur][prev] +=new_flow# reverse edge
            cur = prev
    
    return flow
