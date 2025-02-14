'''
lower time of child indicates that it has a cycle(alternation edge) connection with ancistor
and removing current edge can not disconnect child from ansistor
so current node cant be a articulation point
'''
#%%
from collections import defaultdict

from store_graph import graph_input, draw_graph


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

n=3
inp='''
1 2
1 3
'''

adj = graph_input(inp)
draw_graph(seed=6715)
#%%
visit = defaultdict(lambda : 0)
in_time = defaultdict(lambda : 0)
low_time = defaultdict(lambda : 0)

ap = set()
def dfs(node, parent, timer=1):
    visit[node] = 1
    in_time[node] = timer
    low_time[node] = timer
    
    child = 0
    for child in adj[node]:
        if child == parent: continue
        if visit[child]:# back edge
#                                in_time[child] # what should i do
            low_time[node] = min(low_time[child], low_time[node])
        else:
            timer+=1
            child+=1
            dfs(child, node, timer)
            low_time[node] = min(low_time[node], low_time[child])
            # if in_time[node]>low_time[child]:
            #     # no back connection
            if (not low_time[child]<in_time[node]):# and parent!=-1:# no need as ap is set
                '''
                - if low time is of child less than or equal to root 
                then that means this clind is forming another subtset of graph
                - same node can be ap for 2 different sub graph (look at node 7)
                '''
                ap.add(node)
    if parent == -1 and child>1:
        ''' secrect test case where the graph has only 3 nodes'''
        ap.add(node)

#%%
def find_ap():
    cc = 0
    for i in adj:
        if visit[i]: continue
        dfs(i, -1)
        cc+=1

    print(f'total cc = {cc}')
    for node in ap:
        print(f"articulation point {node}")
    

find_ap()