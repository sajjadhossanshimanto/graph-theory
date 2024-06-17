#%%
from collections import deque
from store_graph import print_grid

#%%
(row, col) = (3, 3)
grid = [
    [0, 1, 0],
    [1, 1, 0],
    [1, 0, 1]
]
# oder   ->   up,    right,   down,    left
movement = [(-1, 0), (0, +1), (+1, 0), (0, -1)]

def is_valid(x, y):
    if x<0 or y<0 or x>=row or y>=col:
        return False
    return True

#%%
level = [[-1]*row for _ in range(col)]# -1 or inf
visit = [[0]*row for _ in range(col)]
def bfs(x, y):
    que = deque([(x, y)])
    visit[x][y] = 1
    dis = 1
    while que:
        x, y = que.popleft()
        # level[x][y] = dis
        for adx, ady in movement:
            cx = x+adx
            cy = y+ady
            
            if not is_valid(cx, cy): continue
            if visit[cx][cy] or (grid[cx][cy]==0): continue
            
            level[cx][cy] = dis
            visit[cx][cy] = 1
            que.append((cx, cy))
        dis += 1

#%%
bfs(1, 1)
# %%
