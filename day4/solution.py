INPUT_FILE = "input.txt"
NUMBERS_LINE = 0
BOARD_SIZE = 5
NOT_OVER = 0


class Board:
    def __init__(self, board: list[list[int]]):
        self.board = board
        self.rows_counter = [0] * BOARD_SIZE
        self.cols_counter = [0] * BOARD_SIZE
        self.unmarked_value = sum((sum(row) for row in board))

    def __repr__(self):
        return repr(self.board)

    def play(self, number: int) -> int:
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == number:
                    self.unmarked_value -= value
                    if self._mark(i, j):
                        return number * self.unmarked_value

                    break

        return NOT_OVER

    def _mark(self, row: int, col: int) -> bool:
        self.rows_counter[row] += 1
        self.cols_counter[col] += 1

        return self.rows_counter[row] == BOARD_SIZE or self.cols_counter[col] == BOARD_SIZE


class BoardManager:
    def __init__(self, boards: list[Board], numbers: list[int]):
        self.boards = boards
        self.numbers = numbers

    def play(self, number: int) -> int:
        winning_score = NOT_OVER
        winning_boards = []
        for i, board in enumerate(self.boards):
            score = board.play(number)
            if score != NOT_OVER:
                winning_boards.append(i)
                winning_score = score

        self.boards = [board for i, board in enumerate(self.boards) if i not in winning_boards]
        return winning_score

    def simulate(self):
        for x in self.numbers:
            score = self.play(x)

            if score != NOT_OVER:
                yield score


def get_input() -> BoardManager:
    def parse_str(string: str, delim: str) -> list[int]:
        return [int(x) for x in string.split(delim) if x != '']

    with open(INPUT_FILE) as f:
        lines = f.read().splitlines()
        numbers = parse_str(lines[NUMBERS_LINE], delim=',')

        boards = []
        for i in range(int(len(lines) / (BOARD_SIZE + 1))):
            board = []
            for j in range(1, BOARD_SIZE + 1):
                line = lines[1 + j + i * (BOARD_SIZE + 1)]
                board.append(parse_str(line, delim=' '))

            boards.append(Board(board))

        return BoardManager(boards, numbers)


def part1_main() -> int:
    game = get_input()
    return next(game.simulate())


def part2_main():
    game = get_input()
    last = NOT_OVER
    for score in game.simulate():
        last = score

    return last


if __name__ == '__main__':
    print(part2_main())
