'''
drid action -> (up, right, down, left)
------------>(increasing x)
|
|
|
(increasing y)
'''
#%%
# row, col = (3, 3)
movement = [(0, -1), (+1, 0), (0 +1), (-1, 0)]
visit = [[0]*3 for i in range(3)]
def dfs(x, y):
    visit[x][y] = 1
    print(visit)
    for adx, ady in movement:
        x+=adx
        y+=ady
        dfs(x, y)

# %%
dfs(0, 0)