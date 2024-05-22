import sys
from export_graph import export_to_tikz
from algorytmy import generate_hamiltonian_graph, generate_non_hamiltonian_graph, find_eulerian_cycle, find_hamiltonian_cycle

def display_help():
    print("\nAvailable commands:")
    print("Help       - Show this message")
    print("Print      - Print the graph in selected representation")
    print("Euler      - Find Eulerian cycle")
    print("Hamilton   - Find Hamiltonian cycle using backtracking")
    print("Export     - Export the graph to TikZ picture")
    print("Exit       - Exit the program (same as Ctrl+C)")

def print_graph(graph):
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

def process_command(command, graph):
    args = command.split()
    cmd = args[0].lower()

    if cmd == 'help':
        display_help()
    elif cmd == 'print':
        print_graph(graph)
    elif cmd == 'euler':
        try:
            print("Eulerian cycle: ", find_eulerian_cycle(graph))
        except Exception as e:
            print(f"Error finding Eulerian cycle: {e}")
    elif cmd == 'hamilton':
        try:
            print("Hamiltonian cycle: ", find_hamiltonian_cycle(graph))
        except Exception as e:
            print(f"Error finding Hamiltonian cycle: {e}")
    elif cmd == 'export':
        if len(args) > 1:
            filename = args[1]
        else:
            filename = "graph.tex"
        export_to_tikz(graph, filename)
    elif cmd == 'exit':
        print('Exiting...')
        sys.exit(0)
    else:
        print('Invalid command. Type "help" for a list of commands.')

def main():
    if len(sys.argv) != 2 or (sys.argv[1] not in ['--hamilton', '--non-hamilton']):
        print("Usage: python3 main.py --hamilton or python3 main.py --non-hamilton")
        sys.exit(1)

    while True:
        try:
            num_nodes = int(input('nodes> '))
            if sys.argv[1] == '--hamilton' and num_nodes <= 10:
                print("Number of nodes must be greater than 10 for Hamiltonian graph")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for number of nodes.")

    if sys.argv[1] == '--hamilton':
        while True:
            try:
                saturation = float(input('saturation> '))
                if saturation not in [30, 70]:
                    print("Saturation must be 30 or 70")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for saturation.")
        graph = generate_hamiltonian_graph(num_nodes, saturation)
    else:
        graph = generate_non_hamiltonian_graph(num_nodes)

    while True:
        try:
            command = input('\naction> ')
            process_command(command, graph)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
