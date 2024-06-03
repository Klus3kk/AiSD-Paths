import os
import time
import matplotlib.pyplot as plt
from algorytmy import generate_hamiltonian_graph, generate_non_hamiltonian_graph, find_eulerian_cycle, find_hamiltonian_cycle
import sys
import numpy as np

sys.setrecursionlimit(10000)  # Ustawienie wyższego limitu rekurencji

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

def smooth_curve(x, y):
    x_new = np.linspace(min(x), max(x), 300)
    y_smooth = np.interp(x_new, x, y)
    return x_new, y_smooth

def plot_results(n_values, euler_times, hamilton_times, title, filename):
    x_euler, y_euler = smooth_curve(n_values, euler_times)
    x_hamilton, y_hamilton = smooth_curve(n_values, hamilton_times)

    plt.figure(figsize=(10, 6))
    plt.plot(x_euler, y_euler, color='b', label='Eulerian Cycle Time', linewidth=1)
    plt.plot(x_hamilton, y_hamilton, color='r', label='Hamiltonian Cycle Time', linewidth=1)
    plt.xlabel('Number of Nodes', fontsize=14)
    plt.ylabel('Time (seconds)', fontsize=14)
    plt.xscale('log')  # Ustawienie skali logarytmicznej dla osi X
    plt.title(title, fontsize=16)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

def plot_results_single(n_values, hamilton_times, title, filename):
    x_hamilton, y_hamilton = smooth_curve(n_values, hamilton_times)

    plt.figure(figsize=(10, 6))
    plt.plot(x_hamilton, y_hamilton, color='r', label='Hamiltonian Cycle Time', linewidth=1)
    plt.xlabel('Number of Nodes', fontsize=14)
    plt.ylabel('Time (seconds)', fontsize=14)
    plt.xscale('log')  # Ustawienie skali logarytmicznej dla osi X
    plt.title(title, fontsize=16)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)

    n_values = [2**i for i in range(1, 10)]  # Dostosowane do mniejszego zakresu

    # Benchmark dla grafów Hamiltona z nasyceniem 70%
    euler_times_70, hamilton_times_70 = benchmark_hamiltonian(n_values, 70)
    plot_results(n_values, euler_times_70, hamilton_times_70, 'Hamiltonian Graphs with 70% Saturation', 'data/hamiltonian_70.png')

    # Benchmark dla grafów nie-hamiltonowskich
    hamilton_times_non = benchmark_non_hamiltonian(n_values)
    plot_results_single(n_values, hamilton_times_non, 'Non-Hamiltonian Graphs with 50% Saturation', 'data/non_hamiltonian_50.png')
