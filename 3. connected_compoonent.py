from store_graph import graph_input, draw_graph

n = 8
# cc 2
inp = '''1 5
5 6
5 2
6 8
2 8
6 4
3 7'''

n=8
# cc = 3
inp='''
1 2
2 3
2 4
3 5
6 7
'''

adj_list = graph_input(inp, n)
# print(p)
draw_graph()

visited = [0]*(n+1)
def dfs(node):
    visited[node]=1
    for i in adj_list[node]:
        if not visited[i]: dfs(i)

cc=0
for i in range(1, n+1):
    if visited[i]: continue
    dfs(i)
    cc+=1

print(cc)
