'''
TODO: how do i determined witch prime function to use.
to me it was a hard question
'''
#%%
from store_graph import G, draw_graph

#%%
n = 9999

def isValid(a, b):
    return len(list(filter(lambda x:x[0]==x[1], zip(str(a), str(b)))))==1

def isPrime(num):
    if num&1==0: return False
    for i in range(2, int(num**.5)):
        if num%i==0: return False
    return True

adj = [[] for _ in range(n+1)]
primes = []
def build_graph():
    for i in range(1000, n+1):
        if isPrime(i):
            primes.append(i)
            G.add_node(i)

    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            a = primes[i]
            b = primes[j]
            if isValid(a, b):
                adj[a].append(b)
                adj[b].append(a)
                
                G.add_edge(a, b)

build_graph()
draw_graph()
#%%
dis = [0]*(n+1)
def bfs(node):
    pass

