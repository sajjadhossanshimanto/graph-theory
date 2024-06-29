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
def find_agmented_path(node="s", agm_path = []):
    agm_path.append(node)
    if node=="t":
        print(agm_path)# logic goes here
        return # avoid marked visit 
    visit[node]=1

    for child, w in adj[node]:        
        if visit[child]: continue
        
        find_agmented_path(child)# memorised. no need to pass variable
        agm_path.pop()

find_agmented_path()


# %%
