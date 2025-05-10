import networkx as nx
from collections import defaultdict

def get_node_levels(graph: nx.DiGraph) -> dict:
    """
    Compute the deepest level for each node in a directed graph using DFS.
    Returns a dictionary where keys are levels and values are lists of nodes
    at their deepest level. Each node appears only in its deepest level.
    
    Args:
        graph: A directed graph (nx.DiGraph)
    
    Returns:
        Dict where keys are integers (levels) and values are lists of nodes
    """
    if not graph.nodes:
        return {}

    # Find source nodes (nodes with no incoming edges)
    source_nodes = [node for node, in_degree in graph.in_degree() if in_degree == 0]
    if not source_nodes:
        source_nodes = list(graph.nodes)

    levels = {}
    visited = set()

    def dfs_level(node, current_level):
        if node in visited:
            return
        levels[node] = current_level
        visited.add(node)
        for neighbor in set(graph.successors(node)):  #sorted(graph.successors(node))
            dfs_level(neighbor, current_level + 1)

    for source in source_nodes:
        dfs_level(source, 0)

    # Group nodes by their levels
    level_to_nodes = defaultdict(list)
    for node, level in levels.items():
        level_to_nodes[level].append(node)
    return dict(level_to_nodes)

# Example Usage
if __name__ == "__main__":
    # Create a directed graph
    G = nx.DiGraph()
    edges = [("T2", "T3"), ("T3", "T4"), ("T4", "T5"), ("T5", "T6"), ("T6", "T7"), ("T3", "T2"), ("T1", "T2"), ("T1", "T3")]
    G.add_edges_from(edges)

    # Get node levels
    levels = get_node_levels(G)

    # Print results
    print("Node levels in the graph:")
    for level, nodes in sorted(levels.items()):
        print(f"Level {level}: {nodes}")
