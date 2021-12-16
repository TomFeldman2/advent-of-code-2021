import heapq

from utils import AoC

Data = list[list[int]]


class ListEntry:
    def __init__(self, row: int, col: int, cost: int):
        self.row = row
        self.col = col
        self.cost = cost

    def __lt__(self, other):
        if not isinstance(other, ListEntry):
            raise NotImplementedError()

        return self.cost < other.cost

    def __repr__(self):
        return f"ListEntry(row={self.row}, col={self.col}, cost={self.cost})"


def parse(string: str) -> Data:
    return [[int(x) for x in line] for line in string.splitlines()]


def part1(data: Data) -> int:
    def neighbors(x: int, y: int) -> list[tuple[int, int]]:
        return list(filter(lambda pos: 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0]), [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]))

    open_list = [ListEntry(row=0, col=0, cost=0)]
    close_set = set()

    while True:
        node = heapq.heappop(open_list)

        if node.row == len(data) - 1 and node.col == len(data[0]) - 1:
            return node.cost

        close_set.add((node.row, node.col))

        for (i, j) in neighbors(node.row, node.col):
            if (i, j) not in close_set and len(list(filter(lambda n: (n.row, n.col) == (i, j), open_list))) == 0:
                heapq.heappush(open_list, ListEntry(row=i, col=j, cost=node.cost + data[i][j]))


def clone_data(data: Data) -> Data:
    return list(map(lambda row: list(map(lambda x: 1 if x == 9 else x + 1, row)), data))


def part2(data: Data) -> int:
    num_rows, num_cols = len(data), len(data[0])

    def neighbors(x: int, y: int) -> list[tuple[int, int]]:
        return list(filter(lambda pos: 0 <= pos[0] < 5 * num_rows and 0 <= pos[1] < 5 * num_cols, [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]))

    open_list = [ListEntry(row=0, col=0, cost=0)]
    visited_set = {(0, 0)}

    while True:
        node = heapq.heappop(open_list)

        if node.row == 5 * num_rows - 1 and node.col == 5 * num_cols - 1:
            return node.cost

        for (i, j) in neighbors(node.row, node.col):
            if (i, j) in visited_set:
                continue

            orig_cost = data[i % num_rows][j % num_cols]
            orig_cost += (int(i // num_rows) + int(j // num_cols))
            if orig_cost > 9:
                orig_cost %= 9

            heapq.heappush(open_list, ListEntry(row=i, col=j, cost=node.cost + orig_cost))
            visited_set.add((i, j))


if __name__ == '__main__':
    aoc = AoC(day=15, parse_fn=parse, part1_fn=part1, part2_fn=part2)
    #     example_data = parse("""1163751742
    # 1381373672
    # 2136511328
    # 3694931569
    # 7463417111
    # 1319128137
    # 1359912421
    # 3125421639
    # 1293138521
    # 2311944581""")
    #     aoc.solve(example_data)

    aoc.solve()
    # aoc.submit()
