'''
supersmart approach
this can also  be done with in and out time but
this approach is better in memory complexity
'''
#%%
from store_graph import graph_input, draw_graph


n = 7
inp = '''
1 2
2 3
2 4
3 7
4 5
4 6
'''
adj_list = graph_input(inp)

#%%
visit = [0]*(n+1)
sub_size = [0]*(n+1)
def dfs(node):
    visit[node] = 1
    size = 1
    for child in adj_list[node]:
        if visit[child]: continue
        size += dfs(child)

    sub_size[node] = size
    return size
dfs(1)
#%%
