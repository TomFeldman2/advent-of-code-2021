from utils import AoC

Data = list[list[int]]

THRESH = 9


def parse(string: str) -> Data:
    return [[int(x) for x in line] for line in string.splitlines()]


def map_data(fn, data: Data) -> Data:
    return list(map(lambda x: list(map(fn, x)), data))


def data_to_str(data: Data) -> str:
    return '\n'.join([''.join(map(lambda x: str(x), line)) for line in data])


def light_neighbors(data: Data, row: int, col: int) -> set[tuple[int, int]]:
    light = set()
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue

            if not (0 <= i < len(data) and 0 <= j < len(data[0])):
                continue

            if data[i][j] < THRESH:
                data[i][j] += 1

                if data[i][j] == THRESH:
                    light.add((i, j))

    return light


def sim_one_step(data: Data) -> tuple[Data, int]:
    light = set()

    for i, nums in enumerate(data):
        for j, num in enumerate(nums):
            if num == THRESH:
                light.add((i, j))

    cnt = 0
    while light:
        cnt += len(light)
        new_lights = set()
        for (i, j) in light:
            new_lights.update(light_neighbors(data, i, j))

        light = new_lights

    return map_data(lambda x: 0 if x == 9 else x + 1, data), cnt


def sim_amount_of_days(data: Data, amount: int) -> int:
    cnt = 0
    for _ in range(amount):
        data, lights = sim_one_step(data)
        cnt += lights

    return cnt


def part1(data: Data) -> int:
    return sim_amount_of_days(data, 100)


def part2(data: Data) -> int:
    pass
    i = 0
    while True:
        if sum(map(lambda x: sum(x), data)) == 0:
            return i

        data, _ = sim_one_step(data)
        i += 1


if __name__ == '__main__':
    aoc = AoC(day=11, parse_fn=parse, part1_fn=part1, part2_fn=part2)

#     example_data = parse("""5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526""")
#     aoc.solve(example_data)

    aoc.solve()
    # aoc.submit()
