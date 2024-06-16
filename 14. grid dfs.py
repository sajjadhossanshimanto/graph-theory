'''
grid action -> (up, right, down, left)
------------>(increasing x)
|
|
|
(increasing y)
'''
#%%
from store_graph import print_grid


#%%
# row, col = (3, 3)
def is_valid(x, y):
    if x<0 or y<0 or x>=3 or y>=3:
        return False
    return True
#              up,    right,   down,    left
# grid system is totally oposit of what we lean in school
movement = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
visit = [[0]*3 for i in range(3)]
def dfs(x, y):
    visit[x][y] = 1
    print_grid(visit)
    for adx, ady in movement:
        cx = x+adx
        cy = y+ady
        if is_valid(cx, cy): dfs(cx, cy)

# %%
dfs(0, 0)