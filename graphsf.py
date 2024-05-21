def initialize_graph(num_nodes, graph_type, saturation=None):
    if graph_type == 'list':
        return {i: [] for i in range(1, num_nodes + 1)}
    elif graph_type == 'matrix':
        return [[0] * num_nodes for _ in range(num_nodes)]
    elif graph_type == 'table':
        return []
    else:
        raise ValueError("Unsupported graph type")

def print_graph(graph):
    for node in graph:
        print(f"{node}: {graph[node]}")
