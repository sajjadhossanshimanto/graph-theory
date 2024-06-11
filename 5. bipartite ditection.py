'''
## concept:
used 'color' theory to ditect bipartite
'''

#%%
from store_graph import graph_input, draw_graph


n=6
inp = '''
1 2
1 6
3 2
3 4
5 6
5 4
'''
adj_list = graph_input(inp, n)

#%%
visit = [0]*(n+1)
color = [1]*(n+1)
def bipart_dfs(node, my_color=0):
    visit[node] = 1
    color[node] = ~my_color# 0 <-> -1
    
    for child in adj_list[node]:
        if visit[child]:
            #check the color
            if color[child]==color[node]: return False
        else:
            bipart_dfs(child, ~my_color)
    
    return True

bipart_dfs(1)
# %%
