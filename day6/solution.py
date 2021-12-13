from functools import lru_cache

from utils import AoC


def parse(string: str) -> list[int]:
    return [int(x) for x in string.split(',')]


@lru_cache(maxsize=None)
def sim_by_formula(days_to_dup: int, amount: int) -> int:
    if amount <= days_to_dup:
        return 0

    amount -= (days_to_dup + 1)
    return 1 + sim_by_formula(6, amount) + sim_by_formula(8, amount)


def sim_one_day(data: list[int]) -> list[int]:
    new_data = []
    for x in data:
        if x == 0:
            new_data.append(6)
            new_data.append(8)
        else:
            new_data.append(x - 1)

    return new_data


def part1(data: list[int]) -> int:
    for _ in range(80):
        data = sim_one_day(data)

    return len(data)


def part2(data: list[int]) -> int:
    sim_res = map(lambda x: sim_by_formula(x, 256), data)
    return sum(sim_res) + len(data)


if __name__ == '__main__':
    aoc = AoC(day=6, parse_fn=parse, part1_fn=part1, part2_fn=part2)
    aoc.submit()
