#%%
inp = '''
3 5 1
2 4 2
1 6 6
1 2 9
3 4 9
4 5 10
4 6 11
2 3 14
5 6 15
'''

n = 8
inp = '''
7 6 1
8 2 2
6 5 2
0 1 4
2 5 4
8 6 6
2 3 7
7 8 7
0 7 8
1 2 8
3 4 9
5 4 10
1 7 11
3 5 14
'''
# ans should be 37


def parse_inp(inp):
    for line in inp.split("\n"):
        if not line: continue
        
        yield list(map(int, line.split(" ")))
    
inp = sorted(parse_inp(inp), key=lambda x:x[2])

#%%
index = [-1]*(n+1)
def find(a):
    # while True:
    #     parent = index[a]
    #     if parent<0: return a# itself is a parent
    #     a=parent

    parent = index[a]
    if parent<0: return a
    
    parent = find(parent)
    # path compration
    index[a]=parent
    return parent

def union(a, b):
    ''' it is confirmed that `a` & `b` do not lies on the same graph 
    
    paramiters:
        a: would be set as parent of b
    '''
    # find works in a constant time, so it would be a proablem
    index[find(b)]=find(a)

#%%
total = 0
graph = []*(n+1)
for a, b, w in inp:
    if find(a)!=find(b):
        union(a, b)
        total += w
        print(a, b, w)

print(total)
# %%
