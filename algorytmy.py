from random import sample

def generate_hamiltonian_graph(num_nodes, saturation):
    graph = {i: [] for i in range(1, num_nodes + 1)}
    nodes = list(range(1, num_nodes + 1))
    hamiltonian_cycle = sample(nodes, num_nodes)

    for i in range(num_nodes):
        graph[hamiltonian_cycle[i]].append(hamiltonian_cycle[(i + 1) % num_nodes])
        graph[hamiltonian_cycle[(i + 1) % num_nodes]].append(hamiltonian_cycle[i])

    edges_needed = int(saturation * (num_nodes * (num_nodes - 1)) / 200) - num_nodes
    while edges_needed > 0:
        u, v = sample(nodes, 2)
        if v not in graph[u]:
            graph[u].append(v)
            graph[v].append(u)
            edges_needed -= 1

    return graph

def generate_non_hamiltonian_graph(num_nodes):
    graph = generate_hamiltonian_graph(num_nodes - 1, 50)
    graph[num_nodes] = []
    return graph

def find_eulerian_cycle(graph):
    def remove_edge(graph, u, v):
        graph[u].remove(v)
        graph[v].remove(u)
    
    stack = []
    cycle = []
    current_vertex = list(graph.keys())[0]
    stack.append(current_vertex)

    while stack:
        if graph[current_vertex]:
            stack.append(current_vertex)
            next_vertex = graph[current_vertex][0]
            remove_edge(graph, current_vertex, next_vertex)
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
