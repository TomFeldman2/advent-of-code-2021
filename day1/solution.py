import numpy as np

INPUT_FILE = "input.txt"
WINDOW_SIZE = 3

def get_input() -> np.array:
    with open(INPUT_FILE) as f:
        return np.array([int(x) for x in f.readlines()])


def count_increases(depths: np.array) -> int:
    depths_1 = np.insert(depths, 0, depths[0])
    depths_2 = np.append(depths, depths[-1])
    diff = depths_2 - depths_1
    return sum([x > 0 for x in diff])


def part1_main():
    return count_increases(get_input())


def part2_main():
    return count_increases(np.convolve(get_input(), np.ones(WINDOW_SIZE, dtype=int), 'valid'))


if __name__ == '__main__':
    print(part2_main())
