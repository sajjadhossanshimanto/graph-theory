from collections import defaultdict
from random import randint

import matplotlib.pyplot as plt
import networkx as nx



# graph_list = [[]]*n
# # llist multipliclation eith object has proablem
# print(graph_list)
# graph_list[3].append(5)
# print(graph_list)


def my_draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=None,
    label_pos=0.5,
    font_size=10,
    font_color="k",
    font_family="sans-serif",
    font_weight="normal",
    alpha=None,
    bbox=None,
    horizontalalignment="center",
    verticalalignment="center",
    ax=None,
    rotate=True,
    clip_on=True,
    rad=0
):
    '''
    code credit: https://stackoverflow.com/questions/22785849/drawing-multiple-edges-between-two-nodes-with-networkx
    '''
    import numpy as np
    
    if ax is None:
        ax = plt.gca()
    if edge_labels is None:
        labels = {(u, v): d for u, v, d in G.edges(data=True)}
    else:
        labels = edge_labels
    text_items = {}
    for (n1, n2), label in labels.items():
        (x1, y1) = pos[n1]
        (x2, y2) = pos[n2]
        (x, y) = (
            x1 * label_pos + x2 * (1.0 - label_pos),
            y1 * label_pos + y2 * (1.0 - label_pos),
        )
        pos_1 = ax.transData.transform(np.array(pos[n1]))
        pos_2 = ax.transData.transform(np.array(pos[n2]))
        linear_mid = 0.5*pos_1 + 0.5*pos_2
        d_pos = pos_2 - pos_1
        rotation_matrix = np.array([(0,1), (-1,0)])
        ctrl_1 = linear_mid + rad*rotation_matrix@d_pos
        ctrl_mid_1 = 0.5*pos_1 + 0.5*ctrl_1
        ctrl_mid_2 = 0.5*pos_2 + 0.5*ctrl_1
        bezier_mid = 0.5*ctrl_mid_1 + 0.5*ctrl_mid_2
        (x, y) = ax.transData.inverted().transform(bezier_mid)

        if rotate:
            # in degrees
            angle = np.arctan2(y2 - y1, x2 - x1) / (2.0 * np.pi) * 360
            # make label orientation "right-side-up"
            if angle > 90:
                angle -= 180
            if angle < -90:
                angle += 180
            # transform data coordinate angle to screen coordinate angle
            xy = np.array((x, y))
            trans_angle = ax.transData.transform_angles(
                np.array((angle,)), xy.reshape((1, 2))
            )[0]
        else:
            trans_angle = 0.0
        # use default box of white with white border
        if bbox is None:
            bbox = dict(boxstyle="round", ec=(1.0, 1.0, 1.0), fc=(1.0, 1.0, 1.0))
        if not isinstance(label, str):
            label = str(label)  # this makes "1" and 1 labeled the same

        t = ax.text(
            x,
            y,
            label,
            size=font_size,
            color=font_color,
            family=font_family,
            weight=font_weight,
            alpha=alpha,
            horizontalalignment=horizontalalignment,
            verticalalignment=verticalalignment,
            rotation=trans_angle,
            transform=ax.transData,
            bbox=bbox,
            zorder=1,
            clip_on=clip_on,
        )
        text_items[(n1, n2)] = t

    ax.tick_params(
        axis="both",
        which="both",
        bottom=False,
        left=False,
        labelbottom=False,
        labelleft=False,
    )

    return text_items

G = nx.DiGraph()
curved_edge_labels = {}
straight_edge_labels = {}
def graph_input(inp, directed=False, weighted = False, node_type = int) -> defaultdict:
    directed = bool(directed)
    weighted = bool(weighted)
    
    G.clear()
    # TODO: build with defaultdict
    graph_list = defaultdict(list)

    for line in inp.split("\n"):
        if not line: continue
        
        v = map(node_type, line.split(" "))
        if weighted: a, b, w = v
        else: a, b = v

        graph_list[a].append((b, w) if weighted else b)
        if not directed:
            graph_list[b].append((a, w) if weighted else a)

        if weighted:        
            if (b, a) in G.edges() and directed:# reverse of current edge(a, b)
                curved_edge_labels[(a, b)] = w
            else:
                straight_edge_labels[(a, b)] = w
            G.add_edge(a,b, weight=w)
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

    # nodes with level
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_labels(G, pos)

    # edges -> straight & curve
    arc_rad = 0.25
    nx.draw_networkx_edges(G, pos, edgelist=straight_edge_labels.keys(), arrows=directed)
    if curved_edge_labels:
        nx.draw_networkx_edges(G, pos, edgelist=curved_edge_labels.keys(), connectionstyle=f'arc3, rad = {arc_rad}', arrows=directed)

    # weights
    if weighted:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=straight_edge_labels, rotate=False)
        if curved_edge_labels:
            my_draw_networkx_edge_labels(G, pos, edge_labels=curved_edge_labels, rotate=False, rad = arc_rad)


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