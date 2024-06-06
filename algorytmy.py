from random import sample, randint

def generate_hamiltonian_graph(num_nodes, saturation):
    if num_nodes <= 0:
        raise ValueError("Number of nodes must be greater than 0")
    if saturation not in [30, 70]:
        raise ValueError("Saturation must be either 30 or 70")

    graph = {i: [] for i in range(1, num_nodes + 1)}
    nodes = list(range(1, num_nodes + 1))

    # Create a Hamiltonian cycle
    hamiltonian_cycle = sample(nodes, num_nodes)
    for i in range(num_nodes):
        u = hamiltonian_cycle[i]
        v = hamiltonian_cycle[(i + 1) % num_nodes]
        graph[u].append(v)
        graph[v].append(u)

    # Add edges to achieve desired saturation
    total_possible_edges = num_nodes * (num_nodes - 1) // 2
    edges_needed = int(saturation * total_possible_edges / 100) - num_nodes

    added_edges = set()
    while edges_needed > 0:
        u, v = sample(nodes, 2)
        if u != v and v not in graph[u]:
            graph[u].append(v)
            graph[v].append(u)
            edges_needed -= 1
            added_edges.add((min(u, v), max(u, v)))

    return graph

def generate_non_hamiltonian_graph(num_nodes, saturation=50):
    if num_nodes <= 1:
        raise ValueError("Number of nodes must be greater than 1")

    graph = {i: [] for i in range(1, num_nodes + 1)}
    nodes = list(range(1, num_nodes + 1))

    # Add edges to achieve desired saturation
    total_possible_edges = num_nodes * (num_nodes - 1) // 2
    edges_needed = int(saturation * total_possible_edges / 100)

    added_edges = set()
    while edges_needed > 0:
        u, v = sample(nodes, 2)
        if u != v and v not in graph[u]:
            graph[u].append(v)
            graph[v].append(u)
            edges_needed -= 1
            added_edges.add((min(u, v), max(u, v)))

    # Ensure there is no Hamiltonian cycle
    isolated_node = randint(1, num_nodes)
    for node in list(graph.keys()):
        if node != isolated_node:
            graph[node] = [v for v in graph[node] if v != isolated_node]
    graph[isolated_node] = []

    return graph

def find_eulerian_cycle(graph):
    def remove_edge(g, u, v):
        g[u].remove(v)
        g[v].remove(u)

    graph_copy = {node: neighbors[:] for node, neighbors in graph.items()}
    stack = []
    cycle = []
    current_vertex = list(graph_copy.keys())[0]
    stack.append(current_vertex)

    while stack:
        if graph_copy[current_vertex]:
            stack.append(current_vertex)
            next_vertex = graph_copy[current_vertex][0]
            remove_edge(graph_copy, current_vertex, next_vertex)
            current_vertex = next_vertex
        else:
            cycle.append(current_vertex)
            current_vertex = stack.pop()

    return cycle

def is_valid_vertex(v, pos, path, graph):
    if v not in graph[path[pos - 1]]:
        return False
    if v in path:
        return False
    return True

def hamiltonian_cycle_util(graph, path, pos):
    if pos == len(graph):
        if path[0] in graph[path[pos - 1]]:
            return True
        return False

    for vertex in graph:
        if is_valid_vertex(vertex, pos, path, graph):
            path[pos] = vertex
            if hamiltonian_cycle_util(graph, path, pos + 1):
                return True
            path[pos] = -1

    return False

def find_hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = list(graph.keys())[0]

    if not hamiltonian_cycle_util(graph, path, 1):
        return "No Hamiltonian cycle found"
    return path
