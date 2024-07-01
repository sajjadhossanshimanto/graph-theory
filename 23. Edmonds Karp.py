#%%
'''
1. memory can be reduced: by avoiding `capacity matrix`. 
- use weigght system. maynot be possible actually. even if i want to caltulat residual capacity one the go i need the base capacity

# learnoing 
- we use `weight matrix` when we need both direct and reverse edge
'''

#%%
from collections import deque, defaultdict
from store_graph import graph_input, draw_graph


inp = '''
s a 7
s d 4
a b 5
a c 3
c b 3
d a 3
d c 2
c t 5
b t 8
'''

graph_input(inp, directed=1, weighted=1, node_type=str)
draw_graph(0, 1, 1, seed=8268)
#%%
def bfs(s, t):
    n = len(capacity)
    trace_back= []# need for backtracking
    
    q = deque()# [(node, incoming_flow), ....]
    q.append([s, float('inf')])
    bottleneck = float("inf")
    while q:
        node, flow = q.popleft()
        trace_back.append(node)
        bottleneck = min(bottleneck, flow)
        
        for child in adj[node]:
            if child not in trace_back and capacity[node][child]:
                if child==t: 
                    return bottleneck, trace_back
                q.append((child, capacity[node][child]))

def max_flow(s, t):
    flow = 0

    while 1:# as long as no more flow available
        r = bfs(s, t)
        if not r: break
        new_flow, parent = r
        flow+=new_flow
        
        # back tracking
        cur = t
        while cur!=s:
            prev = parent.pop()
            capacity[prev][cur] -= new_flow# direct edge
            capacity[cur][prev] +=new_flow# reverse edge
            cur = prev

    return flow

#%%
adj = defaultdict(list)
capacity = defaultdict(dict)
for line in inp.split("\n"):
    if not line: continue
    
    u, v, w = line.split(" ")
    w = int(w)
    adj[u].append(v)
    capacity[u][v] = w
    capacity[v][u] = -w

#%%
print(max_flow("s", "t"))
# %%
