from data_loader import fetch_interactions
from network_builder import build_network_graphs
from visualizer import visualize_graph

def main():
    # Step 1: Ask the user for a protein ID
    protein_id = input("🔍 Enter a protein ID (e.g., TP53): ").strip()
    if not protein_id:
        print("Invalid protein ID entered, please try again.")
        return

    # Step 2: Fetch protein interaction data
    print(f"Fetching interactions for: {protein_id}")
    df = fetch_interactions(protein_id)

    # Step 3: Build the network graph
    min_score = 0.7  # You can also make this user-defined later
    print(f"Building graph with min score: {min_score}")
    G = build_network_graphs(df, min_score=min_score)

    # Step 4: Visualize the graph
    print(f"Visualizing graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
    visualize_graph(G, title=f"{protein_id} Interaction Network")

if __name__ == "__main__":
    main()