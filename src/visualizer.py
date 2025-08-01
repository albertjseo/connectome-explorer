'''
This module visualizes protein interactions.
'''
import matplotlib.pyplot as plt
import networkx as nx

def visualize_graph(G, title="Protein Interaction Network"):
    pos = nx.spring_layout(G, k=0.5, iterations=50, seed=42)
    weights = [G[u][v]['weight'] for u, v in G.edges()]

    plt.figure(figsize=(12, 8))
    nx.draw_networkx_nodes(G, pos, node_size=300, node_color='skyblue')
    nx.draw_networkx_edges(G, pos, width=1, edge_color=weights, edge_cmap=plt.cm.Blues)
    nx.draw_networkx_labels(G, pos, font_size=10)
    plt.title(title)
    plt.axis('off')
    plt.show()