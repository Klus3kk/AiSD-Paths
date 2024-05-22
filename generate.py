import os
import random

def generate_random_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]

def save_to_file(numbers, filename):
    with open(filename, 'w') as file:
        for number in numbers:
            file.write(f"{number}\n")

def generate_files_with_random_numbers():
    os.makedirs('data/files', exist_ok=True)

    n_values = [2**i for i in range(1, 20)]  # Tu zmieniasz, jakiej wielkości pliki chcesz wygenerować

    for n in n_values:
        numbers = generate_random_numbers(n)
        filename = f"data/files/random_numbers_{n}.txt"
        save_to_file(numbers, filename)
        print(f"File {filename} generated with {n} random numbers.")

if __name__ == "__main__":
    generate_files_with_random_numbers()
