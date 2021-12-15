from utils import AoC

FOLD_X = True

Dots = set[tuple[int, ...]]

Folds = list[tuple[bool, int]]

Data = tuple[Dots, Folds]


def parse(string: str) -> Data:
    def parse_fold(f: str) -> tuple[bool, int]:
        axis, pos = f.split(' ')[-1].split('=')
        return axis == 'x', int(pos)

    dots, folds = string.split('\n\n')

    return set([tuple([int(x) for x in dot.split(',')]) for dot in dots.splitlines()]), [parse_fold(fold) for fold in folds.splitlines()]


def fold_half(dots: Dots, fold: tuple[bool, int]) -> Dots:
    is_x_axis, pos = fold

    def get_mirror_cord(x: int, y: int) -> tuple[int, int]:
        xx, yy = x, y
        if not is_x_axis:
            x, y = y, x

        x = pos - (x - pos)

        if not is_x_axis:
            x, y = y, x

        return x, y

    def is_bottom_half(x: int, y: int) -> bool:
        if not is_x_axis:
            x, y = y, x

        return x >= pos

    return set(map(lambda cord: get_mirror_cord(*cord) if is_bottom_half(*cord) else cord, dots))


def dots_to_str(dots: Dots) -> str:
    width = max(map(lambda d: d[0], dots)) + 1
    height = max(map(lambda d: d[1], dots)) + 1

    board = [['.'] * width for _ in range(height)]

    for (x, y) in dots:
        board[y][x] = '#'

    return '\n'.join([''.join(row) for row in board])


def part1(data: Data) -> int:
    dots, folds = data
    dots = fold_half(dots, folds[0])

    return len(dots)


def part2(data: Data) -> int:
    dots, folds = data
    for fold in folds:
        dots = fold_half(dots, fold)

    print(dots_to_str(dots))
    return len(dots)


if __name__ == '__main__':
    aoc = AoC(day=13, parse_fn=parse, part1_fn=part1, part2_fn=part2)

#     example_data = parse("""6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0
#
# fold along y=7
# fold along x=5""")
#
#     aoc.solve(example_data)

    aoc.solve()
    # aoc.submit()
