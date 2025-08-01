'''
This module iterates through the df rows and extracts the protein-protein interaction network.
'''
import networkx as nx

def build_network_graphs(df, min_score=0.0):
    network_graph = nx.Graph()

    for index, row in df.iterrows():
        source = row['preferredName_A']
        target = row['preferredName_B']
        score = row['score']

        if score >= min_score:
            network_graph.add_edge(source, target, weight=score)

    return network_graph