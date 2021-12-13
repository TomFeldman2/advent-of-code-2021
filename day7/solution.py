from math import sqrt

from utils import AoC

Data = list[int]


def parse(string: str) -> Data:
    return [int(x) for x in string.split(',')]


def part1(data: Data) -> int:
    align_pos = sorted(data)[int(len(data) / 2)]
    return sum(map(lambda x: abs(x - align_pos), data))


def part2(data: Data) -> int:

    def fuel(curr_pos: int, move_pos: int) -> int:
        dist = abs(curr_pos - move_pos)
        return int(dist * (dist + 1) / 2)

    def calc_fuel(move_pos: int) -> int:
        return sum(map(lambda x: fuel(x, move_pos), data))

    last = max(data)
    min_fuel = calc_fuel(last)

    for i in range(min(data), last):
        curr_fuel = calc_fuel(i)
        if curr_fuel < min_fuel:
            min_fuel = curr_fuel

    return min_fuel


if __name__ == '__main__':
    aoc = AoC(day=7, parse_fn=parse, part1_fn=part1, part2_fn=part2)
    # aoc.solve([16, 1, 2, 0, 4, 2, 7, 1, 2, 14])
    aoc.solve()
    # aoc.submit()
