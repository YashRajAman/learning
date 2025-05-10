import networkx as nx
from collections import defaultdict, deque
import random
def get_node_and_edge_levels(graph: nx.DiGraph) -> tuple:
    """
    Compute the deepest level for each node in a directed graph using iterative DFS
    and collect edges between consecutive levels. Returns a tuple of two dictionaries:
    - First dict: keys are levels, values are lists of nodes at that level.
    - Second dict: keys are levels, values are lists of edges from level n-1 to level n.
    
    Args:
        graph: A directed graph (nx.DiGraph)
    
    Returns:
        Tuple of (node_levels, edge_levels) dictionaries
    """
    # Handle empty graph
    if not graph.nodes:
        return ({}, {})

    # Find all source nodes (nodes with no incoming edges)
    source_nodes = [node for node, in_degree in graph.in_degree() if in_degree == 0]
    if not source_nodes:
        source_nodes = list(graph.nodes)

    # Initialize variables
    node_max_level = {}  # Tracks max level for each node
    node_state = {node: 'unvisited' for node in graph.nodes}  # unvisited, in_progress, processed
    stack = deque([(node, 0, None) for node in source_nodes])  # (node, level, parent)

    # Iterative DFS to compute max level for each node
    while stack:
        current_node, current_level, parent = stack.pop()  # DFS uses pop (LIFO)

        # If node is being processed (in_progress), check if we can finalize it
        if node_state[current_node] == 'in_progress':
            # Mark as processed if all successors are processed or no deeper paths
            all_successors_done = all(
                node_state.get(neighbor, 'unvisited') == 'processed' or
                node_max_level.get(neighbor, -1) >= current_level + 1
                for neighbor in graph.successors(current_node)
            )
            if all_successors_done:
                node_state[current_node] = 'processed'
            continue

        # If unvisited, start processing
        if node_state[current_node] == 'unvisited':
            node_state[current_node] = 'in_progress'
            # Update max level
            node_max_level[current_node] = max(node_max_level.get(current_node, -1), current_level)
            # Push current node back to finalize later
            stack.append((current_node, current_level, None))
            # Push successors
            for neighbor in graph.successors(current_node):
                if node_state[neighbor] != 'processed':
                    stack.append((neighbor, current_level + 1, current_node))

    # Group nodes by their max level
    level_to_nodes = defaultdict(list)
    for node, level in node_max_level.items():
        level_to_nodes[level].append(node)
    level_to_nodes = dict(sorted(level_to_nodes.items()))

    # Create a set of all graph edges for efficient lookup
    graph_edges = set(graph.edges())

    # Collect edges between consecutive levels
    edge_levels = defaultdict(list)
    max_level = max(level_to_nodes.keys(), default=0)
    for level in range(1, max_level + 1):
        prev_level_nodes = level_to_nodes.get(level - 1, [])
        current_level_nodes = level_to_nodes.get(level, [])
        for src in prev_level_nodes:
            for tgt in current_level_nodes:
                if (src, tgt) in graph_edges:
                    edge_levels[level].append((src, tgt))


    nodes_with_edges = {}
    print("Node and edges levels in the graph:")
    scripts_tracker = set()
    for level in level_to_nodes.keys():
        # print(f"Level {level}: {nodes}")
        node = level_to_nodes.get(level)
        edges = edge_levels.get(level+1, [])
        script_names = []
        if len(edges) > 0:
            for edge in edges:
                script = graph.edges[edge]['script_name']
                print(edge, script)
                if script in scripts_tracker:
                    continue

                script_names.append(script)
        scripts_tracker.update(script_names)
        nodes_with_edges[level] = node + script_names

    return nodes_with_edges

# Example: Create a directed graph with specified edges
if __name__ == "__main__":
    # Create a directed graph
    script_names = ['text1.txt', 'btex.bteq', 'informatica.infa', 'thisthat.nope']
    G = nx.DiGraph()
    edges = [
        ("T1", "T2", 'text1.txt'), ("T1", "T3", 'btex.bteq'), ("T2", "T3", 'informatica.infa'), ("T3", "T2", 'thisthat.nope'),
        ("T3", "T4", 'btex.bteq'), ("T4", "T5", 'text1.txt'), ("T5", "T6", 'thisthat.nope'), ("T6", "T7", 'thisthat.nope')
    ]
    for edge in edges:
        G.add_edge(edge[0], edge[1], script_name=edge[2])

    # Get node and edge levels
    node_levels = get_node_and_edge_levels(G)

    # Print node levels
    # nodes_with_edges = {}
    # print("Node and edges levels in the graph:")
    # for level, nodes in node_levels.items():
    #     # print(f"Level {level}: {nodes}")
    #     node = node_levels.get(level)
    #     edges = edge_levels.get(level+1, [])
    #     print(node, edges)
    #     nodes_with_edges[level] = node + edges

    # Print edges between levels
    # print("\nEdges between levels:")
    # for level, edges in sorted(edge_levels.items()):
    #     print(f"Level {level}: {edges}")

    print(node_levels)