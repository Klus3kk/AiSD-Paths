from random import sample, randint

def generate_hamiltonian_graph(num_nodes, saturation):
    # Inicjalizacja grafu
    graph = {i: [] for i in range(1, num_nodes + 1)}
    nodes = list(range(1, num_nodes + 1))
    
    # Tworzenie cyklu Hamiltona
    hamiltonian_cycle = sample(nodes, num_nodes)
    for i in range(num_nodes):
        u = hamiltonian_cycle[i]
        v = hamiltonian_cycle[(i + 1) % num_nodes]
        graph[u].append(v)
        graph[v].append(u)
    
    # Obliczanie liczby potrzebnych krawędzi do osiągnięcia nasycenia
    total_possible_edges = num_nodes * (num_nodes - 1) // 2
    edges_needed = int(saturation * total_possible_edges / 100) - num_nodes

    added_edges = set()
    
    # Dodawanie dodatkowych krawędzi do osiągnięcia nasycenia
    while edges_needed > 0:
        u, v = sample(nodes, 2)
        if u != v and v not in graph[u]:
            graph[u].append(v)
            graph[v].append(u)
            edges_needed -= 1
            added_edges.add((min(u, v), max(u, v)))
    
    # Dopasowanie stopni wierzchołków do parzystych
    for node in graph:
        while len(graph[node]) % 2 != 0:
            for neighbor in nodes:
                if neighbor != node and neighbor not in graph[node]:
                    graph[node].append(neighbor)
                    graph[neighbor].append(node)
                    added_edges.add((min(node, neighbor), max(node, neighbor)))
                    break

    return graph





def generate_non_hamiltonian_graph(num_nodes):
    graph = generate_hamiltonian_graph(num_nodes - 1, 50)
    isolated_node = num_nodes
    graph[isolated_node] = []
    for node in range(1, num_nodes):
        graph[node].append(isolated_node)
        graph[isolated_node].append(node)
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
    for node in path:
        if node == v:
            return False
    return True

def hamiltonian_cycle_util(graph, path, pos):
    if pos == len(graph):
        if path[0] in graph[path[pos - 1]]:
            return True
        else:
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
