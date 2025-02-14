'''
practise proablem from spoj
TODO: how do i determined witch prime function to use.
to me it was a hard question
'''
#%%
from store_graph import G, draw_graph
from collections import deque, defaultdict

#%%
n = 9999

def isValid(a, b):
    return len(list(filter(lambda x:x[0]==x[1], zip(str(a), str(b)))))==1

def isPrime(num):
    if num&1==0: return False
    for i in range(2, int(num**.5)):
        if num%i==0: return False
    return True

adj = defaultdict(list)
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
#%%
draw_graph()
#%%
dis = defaultdict(lambda : 0)
visit = defaultdict(lambda : 0)
def bfs(node):
    visit[node] = 1
    queue = deque([node])
    level = 1
    while queue:
        node=queue.popleft()
        for child in adj[node]:
            if visit[child]: continue
            
            visit[child] = 1
            queue.append(child)
            dis[child]=level
        level+=1
#%%
a, b = map(int, input().split(" "))
print(abs(dis[b]-dis[a]))