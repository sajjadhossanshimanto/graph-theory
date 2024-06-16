#%%
from store_graph import print_grid


#%%
row, col = (3, 3)
grid = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
# valid movements up, right, down, left
movement = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
#%%
def is_valid(x, y):
    if x<0 or y<0 or x>row or y>col:
        return False
    return True

visit = [[0]*row for _ in range(col)]
def dfs(x, y):
    visit[x][y] = 1
    
    for adx, ady in movement:
        cx = x+adx
        cy = y+ady
        if not is_valid(cx, cy): continue
        if visit[cx][cy]: continue# one lise if condition is faulty
        
        dfs(cx, cy)

cc=0
for x in range(col):
    for y in range(row):
        if visit[x][y] or grid[x][y]==0: continue
        dfs(x, y)
        
        print(x, y)
        cc+=1

print(cc)
# %%
