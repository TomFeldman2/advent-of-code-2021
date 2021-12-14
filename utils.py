from typing import Callable, TypeVar, Optional

from aocd.models import Puzzle

ParseRes = TypeVar('ParseRes')
Fn = Callable[[ParseRes], int]


class AoC:

    def __init__(self, day: int, parse_fn: Callable[[str], ParseRes], part1_fn: Fn, part2_fn: Fn):
        self.puzzle = Puzzle(year=2021, day=day)
        self.part1_fn = part1_fn
        self.part2_fn = part2_fn

        self.data = parse_fn(self.puzzle.input_data)

        self.res1, self.res2 = None, None

    def solve(self, data: Optional[ParseRes] = None):
        ds = data if data else self.data
        res1 = self.part1_fn(ds)
        res2 = self.part2_fn(ds)

        if res1 is not None:
            print(f"first result is {res1}")

        if res2 is not None:
            print(f"second result is {res2}")

        if res1 is None and res2 is None:
            print("not implemented yet")


        if data is None:
            self.res1, self.res2 = res1, res2

        return res1, res2


    def submit(self):
        if self.res2:
            print("submitting part 2")
            self.puzzle.answer_b = self.res2

        elif self.res1:
            print("submitting part 1")
            self.puzzle.answer_a = self.res1

        else:
            print("nothing to submit")
