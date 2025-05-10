import sqlglot
import networkx as nx
import matplotlib.pyplot as plt

def build_lineage_graph(expression, graph=None, parent=None, prefix="root"):
    if graph is None:
        graph = nx.DiGraph()

    node_label = f"{prefix}: {expression.__class__.__name__}"

    if hasattr(expression, "args") and "expressions" in expression.args:
        # For things like WITH or SELECT columns
        for i, sub_expr in enumerate(expression.args["expressions"] or []):
            child_label = f"{node_label} -> exp[{i}]"
            graph.add_edge(node_label, f"{child_label}: {sub_expr.__class__.__name__}")
            build_lineage_graph(sub_expr, graph, node_label, prefix=child_label)

    if hasattr(expression, "args"):
        for key, value in expression.args.items():
            if isinstance(value, sqlglot.Expression):
                child_label = f"{node_label} -> {key}"
                graph.add_edge(node_label, f"{child_label}: {value.__class__.__name__}")
                build_lineage_graph(value, graph, node_label, prefix=child_label)
            elif isinstance(value, list):
                for idx, item in enumerate(value):
                    if isinstance(item, sqlglot.Expression):
                        child_label = f"{node_label} -> {key}[{idx}]"
                        graph.add_edge(node_label, f"{child_label}: {item.__class__.__name__}")
                        build_lineage_graph(item, graph, node_label, prefix=child_label)

    return graph


def visualize_graph(graph):
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, font_size=8, node_size=2000, node_color="lightblue", arrows=True)
    plt.title("SQL AST Lineage Graph")
    plt.show()


# Example complex SQL with INSERT + SELECT
sql = """
INSERT INTO orders (user_id, item)
SELECT id, 'Book'
FROM users
WHERE email = 'alice@example.com';
"""

expression = sqlglot.parse_one(sql, read='postgres')
graph = build_lineage_graph(expression)
visualize_graph(graph)
