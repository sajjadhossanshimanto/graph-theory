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


def parse_inp(inp):
    for line in inp.split("\n"):
        if not line: continue
        
        yield list(map(int, line.split(" ")))
    
inp = sorted(parse_inp(inp), key=lambda x:x[2])

#%%
total = 0
graph = set()# djset
for a, b, w in inp:
    if (a not in graph) or (b not in graph):
        graph.add(a)
        graph.add(b)
        total += w
        

print(total)
# %%
