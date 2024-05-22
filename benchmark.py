# PÓKI CO NIE DZIAŁA, NAPRAWIĘ PÓŹNIEJ!
import os
import time
import matplotlib.pyplot as plt
from algorytmy import generate_hamiltonian_graph, generate_non_hamiltonian_graph, find_eulerian_cycle, find_hamiltonian_cycle

def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return [int(line.strip()) for line in file]

def measure_time(function, *args):
    start_time = time.time()
    result = function(*args)
    end_time = time.time()
    return end_time - start_time, result

def benchmark_hamiltonian(n_values, saturation):
    euler_times = []
    hamilton_times = []

    for n in n_values:
        graph = generate_hamiltonian_graph(n, saturation)
        euler_time, _ = measure_time(find_eulerian_cycle, graph)
        hamilton_time, _ = measure_time(find_hamiltonian_cycle, graph)
        euler_times.append(euler_time)
        hamilton_times.append(hamilton_time)

    return euler_times, hamilton_times

def benchmark_non_hamiltonian(n_values):
    hamilton_times = []

    for n in n_values:
        graph = generate_non_hamiltonian_graph(n)
        hamilton_time, _ = measure_time(find_hamiltonian_cycle, graph)
        hamilton_times.append(hamilton_time)

    return hamilton_times

def plot_results(n_values, euler_times, hamilton_times, title, filename):
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, euler_times, marker='o', linestyle='-', color='b', label='Eulerian Cycle Time')
    plt.plot(n_values, hamilton_times, marker='s', linestyle='--', color='r', label='Hamiltonian Cycle Time')
    plt.xlabel('Number of Nodes', fontsize=14)
    plt.ylabel('Time (seconds)', fontsize=14)
    plt.title(title, fontsize=16)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

def plot_results_single(n_values, hamilton_times, title, filename):
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, hamilton_times, marker='s', linestyle='--', color='r', label='Hamiltonian Cycle Time')
    plt.xlabel('Number of Nodes', fontsize=14)
    plt.ylabel('Time (seconds)', fontsize=14)
    plt.title(title, fontsize=16)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)

    filenames = [f"data/files/random_numbers_{2**i}.txt" for i in range(1, 8)]  # Adjusted to a smaller range
    n_values = [2**i for i in range(1, 8)]

    for filename in filenames:
        if os.path.exists(filename):
            numbers = read_numbers_from_file(filename)
            print(f"Read {len(numbers)} numbers from {filename}")
        else:
            print(f"File {filename} does not exist.")

    # Benchmark for Hamiltonian graphs with saturation 30
    euler_times, hamilton_times = benchmark_hamiltonian(n_values, 30)
    plot_results(n_values, euler_times, hamilton_times, 'Hamiltonian Graphs with 30% Saturation', 'data/hamiltonian_30.png')

    # Benchmark for non-Hamiltonian graphs
    hamilton_times_non = benchmark_non_hamiltonian(n_values)
    plot_results_single(n_values, hamilton_times_non, 'Non-Hamiltonian Graphs with 50% Saturation', 'data/non_hamiltonian_50.png')
