import functools

from utils import AoC

Data = list[list[int]]


def parse(string: str) -> Data:
    return [[int(x) for x in list(line)] for line in string.splitlines()]


def is_in_bounds(data: Data, row: int, col: int) -> bool:
    return 0 <= row < len(data) and 0 <= col < len(data[0])

def get_mins(data: Data) -> list[tuple[int, int]]:
    def is_lt(val: int, row: int, col: int) -> bool:
        if not is_in_bounds(data, row, col):
            return True

        return val < data[row][col]

    mins = []
    for i, nums in enumerate(data):
        for j, value in enumerate(nums):
            if all((is_lt(value, i + 1, j), is_lt(value, i - 1, j), is_lt(value, i, j + 1), is_lt(value, i, j - 1))):
                mins.append((i, j))

    return mins


def part1(data: Data) -> int:
    mins = get_mins(data)
    return sum(map(lambda x: data[x[0]][x[1]], mins)) + len(mins)


def compute_basin(data: Data, row: int, col: int) -> int:
    computed, specials = [], []
    not_computed = [(row, col)]

    def add_to_basin(curr_val: int, next_i: int, next_j: int):
        if not is_in_bounds(data, next_i, next_j) or (next_i, next_j) in computed:
            return

        next_val = data[next_i][next_j]
        if next_val == 9:
            return

        if next_val > curr_val:
            not_computed.append((next_i, next_j))

        else:
            specials.append((next_i, next_j))

        return

    while not_computed:
        i, j = not_computed.pop()

        if (i, j) in computed:
            continue

        computed.append((i, j))
        val = data[i][j]

        for (ii, jj) in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            add_to_basin(val, ii, jj)

    return len(computed) + len(set(specials).difference(computed))


def part2(data: Data) -> int:
    basins = [0] * 3

    def insert_to_basins(val: int) -> None:
        smallest = min(basins)

        if val > smallest:
            basins.remove(smallest)
            basins.append(val)

        return

    for (i, j) in get_mins(data):
        basin_size = compute_basin(data, i, j)
        insert_to_basins(basin_size)

    return basins[0] * basins[1] * basins[2]


if __name__ == '__main__':
    aoc = AoC(day=9, parse_fn=parse, part1_fn=part1, part2_fn=part2)

#     example_data = parse("""2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678""")
#     aoc.solve(example_data)

    aoc.solve()
    aoc.submit()
