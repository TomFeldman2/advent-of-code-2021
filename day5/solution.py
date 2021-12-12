from collections import defaultdict

INPUT_FILE = "input.txt"


class Cord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Cord(x={self.x}, y={self.y})"

    def __str__(self):
        return str((self.x, self.y))

def get_input() -> list[tuple[Cord, Cord]]:
    with open(INPUT_FILE) as f:
        lines = f.read().splitlines()
        cord_list = []

        def convert_cord_to_int(cord: str) -> Cord:
            start, end = cord.split(',')
            return Cord(int(start), int(end))

        for line in lines:
            first, second = line.split(' -> ')
            cord_list.append((convert_cord_to_int(first), convert_cord_to_int(second)))

        return cord_list
    
def generate_board() -> dict:
    return defaultdict(lambda: 0)

def mark(board: dict[tuple[int, int], int], first: Cord, second: Cord) -> None:
    dx = 1 if first.x < second.x else (0 if first.x == second.x else -1)
    dy = 1 if first.y < second.y else (0 if first.y == second.y else -1)
    x, y = first.x, first.y

    steps = max(abs(first.x - second.x), abs(first.y - second.y)) + 1

    for _ in range(steps):
        board[x, y] += 1
        x += dx
        y += dy

def cnt_board(board: dict[tuple[int, int], int]) -> int:
    return len(list(filter(lambda x: x > 1, board.values())))


def part1_main() -> int:
    cords = get_input()

    board = generate_board()
    for first, second in cords:
        if first.x == second.x or first.y == second.y:
            mark(board, first, second)

    return cnt_board(board)


def part2_main():
    cords = get_input()

    board = generate_board()

    for first, second in cords:
        mark(board, first, second)

    return cnt_board(board)


if __name__ == '__main__':
    print(part2_main())
