'''
grid action -> (up, right, down, left)
------------>(increasing Y)
|
|
|
(increasing X)
'''
#%%
from store_graph import print_grid


#%%
row, col = (3, 3)
def is_valid(x, y):
    if x<0 or y<0 or x>=row or y>=col:
        return False
    return True
#              up,    right,   down,    left
# grid system is totally oposit of what we lean in school
movement = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
visit = [[0]*row for i in range(col)]
def dfs(x, y):
    visit[x][y] = 1
    print_grid(visit)
    for adx, ady in movement:
        cx = x+adx
        cy = y+ady
        if not is_valid(cx, cy): continue
        # if pos is not valid can't even check for visit or not
        
        if visit[cx][cy]: continue
        dfs(cx, cy)
 
# %%
dfs(0, 0)
# %%
