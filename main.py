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
    if not args:
        print("Invalid command. Type 'help' for a list of commands.")
        return

    cmd = args[0].lower()

    if cmd == 'help':
        display_help()
    elif cmd == 'print':
        print_graph(graph)
    elif cmd == 'euler':
        try:
            cycle = find_eulerian_cycle(graph)
            if cycle:
                print("Eulerian cycle: ", cycle)
            else:
                print("No Eulerian cycle found")
        except Exception as e:
            print(f"Error finding Eulerian cycle: {e}")
    elif cmd == 'hamilton':
        try:
            cycle = find_hamiltonian_cycle(graph)
            if cycle:
                print("Hamiltonian cycle: ", cycle)
            else:
                print("No Hamiltonian cycle found")
        except Exception as e:
            print(f"Error finding Hamiltonian cycle: {e}")
    elif cmd == 'export':
        try:
            if len(args) > 1:
                filename = args[1]
            else:
                filename = input("Please enter the filename to export the graph: ")
            filename += '.tex'
            export_to_tikz(graph, filename)
        except Exception as e:
            print(f"Error exporting graph: {e}")
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
                raise ValueError("Number of nodes must be greater than 10 for Hamiltonian graph")
            elif num_nodes < 1:
                raise ValueError("Number of nodes must be at least 1")
            break  # Exit the loop if input is valid
        except ValueError as e:
            print(f"Invalid input: {e}")

    if sys.argv[1] == '--hamilton':
        while True:
            try:
                saturation = float(input('saturation> '))
                if saturation not in [30, 70]:
                    raise ValueError("Saturation must be 30 or 70")
                break  # Exit the loop if input is valid
            except ValueError as e:
                print(f"Invalid input: {e}")
        graph = generate_hamiltonian_graph(num_nodes, saturation)
    else:
        saturation = 50  # Fixed saturation for non-Hamiltonian graph
        graph = generate_non_hamiltonian_graph(num_nodes, saturation)

    while True:
        try:
            command = input('\naction> ')
            process_command(command, graph)
        except ValueError as e:  # Catch specific errors from your functions
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:  # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
