from __future__ import annotations

from typing import Optional

INPUT_FILE = "input.txt"


def get_input() -> list[list[int]]:
    with open(INPUT_FILE) as f:
        return [[int(x) for x in line] for line in f.read().splitlines()]


def transpose(mat: list[list]) -> list[tuple]:
    return list(zip(*mat))


def get_most_common_bits(mat: list[list[int]], index: Optional[int] = None) -> int | list[int]:
    def get_col_most_common(col: tuple | list) -> int:
        return round(1 + sum(col) / len(col)) - 1

    if index is None:
        return list(map(lambda line: get_col_most_common(line), transpose(mat)))

    return get_col_most_common([row[index] for row in mat])


def get_input_with_bit(bit: int):
    assert bit == 0 or bit == 1
    return list(filter(lambda x: x[0] == bit, get_input()))


def decode_bin(gamma_bin: list[int]) -> tuple[int, int]:
    gamma, eps = 0, 0
    for x in gamma_bin:
        gamma = (gamma << 1) + x
        eps = (eps << 1) + 1 - x
    return gamma, eps


def part1_main():
    gamma_bin = get_most_common_bits(get_input())
    gamma, eps = decode_bin(gamma_bin)
    return gamma * eps


def filter_until_one(words: list[list[int]], is_common: bool):
    for i in range(len(words)):
        if len(words) == 1:
            return words[0]

        common_bit = get_most_common_bits(words, i)
        expected_bit = common_bit if is_common else 1 - common_bit

        words = list(filter(lambda word: word[i] == expected_bit, words))


def part2_main():
    mat = get_input()

    oxygen_bin = filter_until_one(mat, True)
    co2_bin = filter_until_one(mat, False)
    oxygen, _ = decode_bin(oxygen_bin)
    co2, _ = decode_bin(co2_bin)
    return oxygen * co2


if __name__ == '__main__':
    print(part2_main())
