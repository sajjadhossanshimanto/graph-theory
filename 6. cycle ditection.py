'''

## terminologies

- used back egde ditection tecnique
'''
#%%
from store_graph import graph_input, draw_graph


n=5
inp='''
1 2
2 3
2 4
4 3
4 5
'''

adj_list = graph_input(inp)
draw_graph()
#%%
visit = [0]*(n+1)
def ditect_edge(node, parent):
    ''' uses dfs call
    returns:
        True if any back edge is detected
        False
    '''
    visit[node]=1
    for child in adj_list[node]:
        if visit[child]:
            if child != parent: return True
        else:
            return ditect_edge(child, node)# TODO: return issue in recursive calls
    
    return False


ditect_edge(1, -1)
# %%
