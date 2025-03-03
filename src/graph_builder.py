import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

def build_knowledge_graph(ner_df):
    """
    Constructs a knowledge graph from Named Entity Recognition (NER) results.
    
    Parameters:
    ner_df (pd.DataFrame): DataFrame with entity recognition results (columns: 'value', 'entity_group', 'sentence').
    
    Returns:
    nx.Graph: A NetworkX graph representing entity relationships.
    """
    G = nx.Graph()
    
    for _, row in ner_df.iterrows():
        entity = row['value']
        entity_group = row['entity_group']
        
        # Add node and edge to represent the entity's category
        G.add_node(entity, label=entity_group)
        G.add_edge(entity, entity_group)
    
    return G

def visualize_graph(G):
    """
    Visualizes the constructed knowledge graph.
    
    Parameters:
    G (nx.Graph): The knowledge graph to visualize.
    """
    plt.figure(figsize=(8,6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, edge_color='gray')
    plt.show()

if __name__ == "__main__":
    # Example NER data
    data = {
        'value': ['COVID-19', 'SARS-CoV-2', 'Fever'],
        'entity_group': ['Disease', 'Virus', 'Symptom'],
        'sentence': ["COVID-19 is caused by SARS-CoV-2.", "Fever is a symptom of COVID-19."]
    }
    ner_df = pd.DataFrame(data)
    
    G = build_knowledge_graph(ner_df)
    visualize_graph(G)
