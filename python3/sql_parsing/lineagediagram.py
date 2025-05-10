import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
import random
import string

# Initialize directed graph
G = nx.DiGraph()

# Generate 200 nodes and cyclic edges
num_nodes = 500
edges = []

for i in range(num_nodes):
    for j in range(2):  # Two edges from each node for density
        target = (i + random.randint(1, num_nodes - 1)) % num_nodes
        src = f"N{i}"
        dst = f"N{target}"
        if src != dst:
            edges.append((src, dst, {"edge_name": f"{src}->{dst}"}))

# Add edges to the graph
G.add_edges_from(edges)

# Layout using Graphviz (dot layout for hierarchy-like structure)
pos = graphviz_layout(G, prog='dot')

# Draw nodes and edges
plt.figure(figsize=(50, 50))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500, arrows=True)

# Draw edge labels from "edge_name"
edge_labels = nx.get_edge_attributes(G, 'edge_name')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Save as high-quality PNG
plt.savefig("cyclic_digraph.png", dpi=300, bbox_inches='tight')
plt.close()

print("Graph saved as cyclic_digraph.png")
