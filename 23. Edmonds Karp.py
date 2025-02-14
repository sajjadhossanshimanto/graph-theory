#%%
'''
1. memory can be reduced: by avoiding `capacity matrix`. 
- use weigght system. maynot be possible actually. even if i want to caltulat residual capacity one the go i need the base capacity
2. for now no need of recidual edge

# learnoing 
- we use `weight matrix` when we need both direct and reverse edge
- in list indexing is pointer
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
    parent= {}# need for backtracking
    
    q = deque()# [(node, incoming_flow), ....]
    q.append([s, float('inf')])
    bottleneck = float("inf")
    while q:
        node_pointer = q.popleft()
        node, flow = node_pointer
        bottleneck = min(bottleneck, flow)
        
        for child_pointer in adj[node]:
            child, w = child_pointer
            if child not in parent and w:
                parent[child] = node_pointer# TODO: node pointer

                if child==t: return bottleneck, parent
                q.append(child_pointer)

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
            prev = parent[cur]
            prev[1] -= new_flow
            cur = prev[0]

    return flow

#%%
adj = defaultdict(list)
# capacity = defaultdict(dict)
for line in inp.split("\n"):
    if not line: continue
    
    u, v, w = line.split(" ")
    w = int(w)
    adj[u].append([v, w])# [node, incoming_flow]# this have tobe nonfrezen

#%%
source = "s"
sink = "t"
print(max_flow(source, sink))
# %%
