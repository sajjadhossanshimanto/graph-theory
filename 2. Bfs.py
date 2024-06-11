from store_graph import graph_list, n, draw_graph
from collections import deque


visit = [0]*n
def bfs(root):
    travel = deque([root]) # Queue: first in first out
    visit[root] = 1
    
    while travel:
        i = travel.popleft()
        print(i)# operation goes here
        for child in graph_list[i]:
            if visit[child]==0:
                travel.append(child)
                visit[child] = 1# mark as vesited before traverse
        # draw_graph()

bfs(4)




### one cummon mistake
