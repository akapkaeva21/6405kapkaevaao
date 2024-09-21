import csv
import sys
import math


def read_config(file_path):
    """Читает конфигурацию из CSV файла."""
    fieldnames = ['n0', 'h', 'nk', 'a', 'b', 'c']
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file, fieldnames=fieldnames, delimiter=",")
        config = next(reader)  # Читаем первую строку
    return {
        'n0': int(config['n0']),
        'h': int(config['h']),
        'nk': int(config['nk']),
        'a': float(config['a']),
        'b': float(config['b']),
        'c': float(config['c']),
    }


def calculate_y(n0, h, nk, a, b, c):
    results = []
    for x in range(n0, nk, h):
        y = (math.sin(a * x + b)) ** 2 + (math.cos(c * x)) ** 2  # Example function
        results.append(y)
    return results

def write_results_to_csv(results, file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['y'])  # Header
        for y in results:
            writer.writerow([y])


def main():
    config_file = 'config'  # Default config file
    if len(sys.argv) > 1:
        config_file = sys.argv[1]  # Override with command line argument

    config = read_config(config_file)

    results = calculate_y(config['n0'], config['h'], config['nk'], config['a'], config['b'], config['c'])
    write_results_to_csv(results, 'results')

main()
