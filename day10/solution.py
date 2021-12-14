from utils import AoC

Data = list[str]

PAREN_SCORE_CORRUPTED = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

PAREN_SCORE_INCOMPLETE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

OPEN_PARENS = ['(', '[', '{', '<']

OPEN_TO_CLOSE = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def is_open_paren(paren: str) -> bool:
    return paren in OPEN_PARENS


def parse(string: str) -> Data:
    return string.splitlines()


def match_top_paren(stack: list[str], paren: str) -> bool:
    if not stack:
        return False

    if paren == stack[-1]:
        stack.pop()
        return True

    return False


def part1(data: Data) -> int:
    cnt = 0
    for line in data:
        stack = []
        for c in line:
            if is_open_paren(c):
                stack.append(OPEN_TO_CLOSE[c])

            elif not match_top_paren(stack, c):
                cnt += PAREN_SCORE_CORRUPTED[c]
                break

    return cnt


def part2(data: Data) -> int:
    scores = []
    for line in data:
        stack = []
        for c in line:
            if is_open_paren(c):
                stack.append(OPEN_TO_CLOSE[c])

            elif not match_top_paren(stack, c):
                break
        else:
            cnt = 0
            for c in reversed(stack):
                cnt *= 5
                cnt += PAREN_SCORE_INCOMPLETE[c]

            scores.append(cnt)

    return sorted(scores)[int(len(scores) / 2)]


if __name__ == '__main__':
    aoc = AoC(day=10, parse_fn=parse, part1_fn=part1, part2_fn=part2)

#     example_data = parse("""[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]""")
#     aoc.solve(example_data)

    aoc.solve()
    aoc.submit()
