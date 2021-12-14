from utils import AoC

Data = list[list[str]]


def parse(string: str) -> Data:
    return [line.split('-') for line in string.splitlines()]

def part1(data: Data) -> int:
    pass


def part2(data: Data) -> int:
    pass


if __name__ == '__main__':
    aoc = AoC(day=12, parse_fn=parse, part1_fn=part1, part2_fn=part2)
    print(aoc.data)

    example_data = parse("""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""")
    aoc.solve(example_data)

    # aoc.solve()
    # aoc.submit()
