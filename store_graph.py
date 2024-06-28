from collections import defaultdict
from random import randint

import matplotlib.pyplot as plt
import networkx as nx



# graph_list = [[]]*n
# # llist multipliclation eith object has proablem
# print(graph_list)
# graph_list[3].append(5)
# print(graph_list)

G = nx.DiGraph()
def graph_input(inp, indexed=1, directed=False, weighted = False) -> defaultdict:
    '''
    eighter 'Zero indexed or 'One' indexed
    for stringly connected conponent `1 2` means 1 has directed edge toowards 2
    '''
    directed = bool(directed)
    weighted = bool(weighted)
    
    G.clear()
    # TODO: build with defaultdict
    graph_list = defaultdict(list)

    for line in inp.split("\n"):
        if not line: continue
        
        v = map(int, line.split(" "))
        if weighted: a, b, w = v
        else: a, b = v

        graph_list[a].append((b, w) if weighted else b)
        if not directed:
            graph_list[b].append((a, w) if weighted else a)
        
        if weighted: G.add_edge(a,b, weight=w, length=w)
        else: G.add_edge(a,b)

    return graph_list

pos = None
def draw_graph(cache=True, directed=False, weighted=False, seed=None):
    ''' 
    - use `cache=False` to forcefully redraw 
    ~ - if you use `seed must enable redrawing`
    '''
    # subax1 = plt.subplot(121)
    global pos

    directed = bool(directed)
    if seed:
        pos = nx.spring_layout(G, seed=seed)
    elif (not cache) or (not pos):
        seed = randint(1000, 9999)
        print(f"seed = {seed}")
        pos = nx.spring_layout(G, seed=seed)

    nx.draw(G, pos, with_labels=True, font_weight='bold', arrows=directed, arrowsize=40, connectionstyle='arc3, rad = 0.1')
    if weighted:
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels)

    plt.show()

def print_grid(matrix):
    # chould have use pandas dataframe print function
    print(*matrix, sep="\n")
    print()

def build_plotly():
    import plotly.graph_objects as go
    
    edge_x = []
    edge_y = []
    pos = nx.spring_layout(G)
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')
    
    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            # colorscale options
            #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>Network graph made with Python',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plotly.com/python/network-graphs/'> https://plotly.com/python/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
    fig.show()