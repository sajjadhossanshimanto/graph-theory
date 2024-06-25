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
