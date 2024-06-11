from store_graph import graph_list, n


visit = [0]*(n+1)# ensuring 1th index
# 0 is not a object so no issue
# print(visit)

# visit[3]=1
# print(visit)

def dfs(root):
    visit[root]=1
    print(root)# log or main logis goes here
    for child in graph_list[root]:
        if visit[child]==1: continue
        dfs(child)

dfs(3)