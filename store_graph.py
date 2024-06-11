from demo_graph import n, inp

import matplotlib.pyplot as plt
import networkx as nx



# graph_list = [[]]*n
# # llist multipliclation eith object has proablem
# print(graph_list)
# graph_list[3].append(5)
# print(graph_list)

G = nx.Graph()
def graph_input(inp, n, indexed=1):
    '''
    eighter 'Zero indexed or 'One' indexed
    '''
    G.clear()
    graph_list = [[] for i in range(n+indexed)]
    for i in range(n+indexed): G.add_node(i)

    for line in inp.split("\n"):
        if not line: continue
        
        a, b = map(int, line.split(" "))
        graph_list[a].append(b)
        graph_list[b].append(a)
        
        G.add_edge(a,b)

    return graph_list

def draw_graph():
    # subax1 = plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
