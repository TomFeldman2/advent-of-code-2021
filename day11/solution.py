from utils import AoC

Data = list[int]


def parse(string: str) -> Data:
    return string


def part1(data: Data) -> int:
    pass


def part2(data: Data) -> int:
    pass


if __name__ == '__main__':
    aoc = AoC(day=11, parse_fn=parse, part1_fn=part1, part2_fn=part2)
    print(aoc.data)
    # aoc.solve(example_data)
    aoc.solve()
    # aoc.submit()
