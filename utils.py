from typing import Callable, TypeVar

from aocd.models import Puzzle

ParseRes = TypeVar('ParseRes')
Fn = Callable[[ParseRes], int]


def main(day: int, parse_fn: Callable[[str], ParseRes], part1_fn: Fn, part2_fn: Fn, submit: bool):
    puzzle = Puzzle(year=2021, day=day)

    def solution():
        ds = parse_fn(puzzle.input_data)
        res1 = part1_fn(ds)
        res2 = part2_fn(ds)
        return res1, res2

    res1, res2 = solution()

    print(f"first result is {res1}")
    print(f"second result is {res2}")
    if res2:
        if submit:
            print("submitting part 2")
            puzzle.answer_b = res2

    elif res1:
        if submit:
            print("submitting part 1")
            puzzle.answer_a = res1
