'''
practise proablem from hacker earth

learning : ditermine either either two nodes are from same cc
'''
# n m
# n -> veriable count
# m -> statment count
n = 5
m = 5
inp = '''
1 = 2
3 = 1
4 != 2
5 = 4
3 != 5
'''

n=3
m=2
inp = '''
2 = 1
3 != 2
'''

from collections import deque


# process input
adj = [[] for _ in range(n+1)]
lines = deque(inp.split())
# m can also be determined from inital length of lines
for _ in range(m):
    line = lines.popleft()
    if "!=" in line:
        lines.append(line)
    else:
        a, b = map(int, line.split(" "))
        adj[a].append(b)
        adj[b].append(a)


# determines cc
visit = [0]*(n+1)
cc_level = [0]*(n+1)
def dfs(node, level=1):
    visit[node] = 1
    for child in adj[node]:
        if visit[child]: continue
        cc_level[child] = level

cc = 1
for node in range(1, n+1):
    if visit[node]: continue
    
    dfs(node, cc)
    cc+=1

# ans query
a, b = map(int, input().split(" "))
if cc_level[a]==cc_level[b]: print("YES")
else: print("NO")


