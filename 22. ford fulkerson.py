#%%
from store_graph import graph_input, draw_graph
from collections import defaultdict


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

# note: though network is directed. create adj considering undirected. because of residual edge
adj = graph_input(inp, directed=1, weighted=1, node_type=str)
#%%
visit = defaultdict(lambda :0)
height_flow = -1
final_flow =[]
def find_agmented_path(node="s", agm_path = [], max_flow=(float('inf'), )):
    global final_flow, height_flow

    agm_path.append(node)
    if node=="t":
        print(agm_path, max_flow)# logic goes here
        if max_flow[0]>height_flow:
            final_flow = agm_path.copy()# pop effected selected final path
            height_flow = max_flow[0]
        visit.clear()# do not remove the visited array. it actually helps to avoid back edge
        return # avoid marked visit 
    visit[node]=1

    for child, w in adj[node]:
        if visit[child]: continue

        w=int(w)
        if w<max_flow[0]: max_flow = (w, child)
        find_agmented_path(child, max_flow=max_flow)# memorised. no need to pass variable
        agm_path.pop()

find_agmented_path()
print("final ->", final_flow)
# can there be any nodes that don't dgoes to sink

# %%
