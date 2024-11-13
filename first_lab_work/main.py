import argparse
import csv
import sys
import math

FIELD_NAMES = ('n0', 'h', 'nk', 'a', 'b', 'c')
FIELD_DEFAULT = (0.0, 1.0, 10.0, 1.0, 2.0, 3.0)


def read_config(file_path: str) -> dict[str, float]:
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file, fieldnames=FIELD_NAMES, delimiter=",")
        for row in reader:
            return {k: float(v) for k, v in  row.items()}
    return {k: v for k, v in zip(FIELD_NAMES, FIELD_DEFAULT)}

def target_func(x: float, a: float, b: float, c: float) -> float:
    return (math.sin(a * x + b)) ** 2 + (math.cos(c * x)) ** 2


def calculate_y(n0: float, h: float, nk: float, a: float, b: float, c: float) -> tuple[tuple[float, float], ...]:
    iterations = int((nk - n0) / h)
    x = n0
    return tuple((x := x + h * index, target_func(x, a, b, c))for index in range(iterations))


def write_results_to_csv(results: tuple[tuple[float, float], ...], file_path: str):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['x', 'y'])  # Header
        for row in results:
            writer.writerow(row)


def write_results_to_txt(results: tuple[tuple[float, float], ...], file_path: str):
    with open(file_path, mode='w') as txt_file:
        print('\n'.join(f'{x:>10.3f},{y:>10.3f}' for x, y in results), file=txt_file)


def csv_config():
    config = read_config('config')
    values = calculate_y(**config)
    write_results_to_txt(values, 'results.txt')
    write_results_to_csv(values, 'results.csv')


def read_cons():
    parser = argparse.ArgumentParser(description='Read configuration parameters.')

    # Определяем ожидаемые аргументы
    parser.add_argument('--n0', type=float, required=True, help='Initial value n0')
    parser.add_argument('--h', type=float, required=True, help='Step size h')
    parser.add_argument('--nk', type=float, required=True, help='Number of steps nk')
    parser.add_argument('--a', type=float, required=True, help='Parameter a')
    parser.add_argument('--b', type=float, required=True, help='Parameter b')
    parser.add_argument('--c', type=float, required=True, help='Parameter c')

    args = parser.parse_args()

    return {
        'n0': args.n0,
        'h': args.h,
        'nk': args.nk,
        'a': args.a,
        'b': args.b,
        'c': args.c,
    }

def main():
    # csv_config()
    # exit(0)

    args = read_cons()

    # Считываем конфигурацию из файла
    #config = read_config(args.config)
    #
    # config_file = 'config'
    # if len(sys.argv) > 1:
    #     config_file = sys.argv[1]
    #
    # config = read_cons(config_file)

    results = calculate_y(**args) #config['n0'], config['h'], config['nk'], config['a'], config['b'], config['c'])
    write_results_to_csv(results, 'results_new')


if __name__ == "__main__":
    main()
