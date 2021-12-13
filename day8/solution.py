from utils import AoC

IN_DIGITS = 10
OUT_DIGITS = 4

Row = tuple[list[str], list[str]]
Data = list[Row]

UNIQUE_SIGS_TO_NUM = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}

SIGS_TO_NUM = {
    frozenset({'a', 'b', 'c', 'e', 'f', 'g'}): 0,
    frozenset({'c', 'f'}): 1,
    frozenset({'a', 'c', 'd', 'e', 'g'}): 2,
    frozenset({'a', 'c', 'd', 'f', 'g'}): 3,
    frozenset({'b', 'c', 'd', 'f'}): 4,
    frozenset({'a', 'b', 'd', 'f', 'g'}): 5,
    frozenset({'a', 'b', 'd', 'e', 'f', 'g'}): 6,
    frozenset({'a', 'c', 'f'}): 7,
    frozenset({'a', 'b', 'c', 'd', 'e', 'f', 'g'}): 8,
    frozenset({'a', 'b', 'c', 'd', 'f', 'g'}): 9,
}


def parse(string: str) -> Data:
    data = []
    for row in string.splitlines():
        in_seg, out_seg = row.split(' | ')
        data.append((in_seg.split(' '), out_seg.split(' ')))

    return data


def parse_example() -> Data:
    example = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

    return parse(example)


def part1(data: Data) -> int:
    cnt = 0
    for in_sigs, out_sigs in data:
        decode_map = {}
        for num in in_sigs:
            sigs = frozenset(list(num))
            if len(sigs) in UNIQUE_SIGS_TO_NUM:
                decode_map[sigs] = UNIQUE_SIGS_TO_NUM[len(sigs)]

        cnt += len(list(filter(lambda x: frozenset(list(x)) in decode_map, out_sigs)))

    return cnt


def decode(in_sigs: list[str]) -> dict[str, str]:
    def get_elem_from_set(s: frozenset[str]) -> str:
        return next(iter(s))

    actual_to_orig = {}
    unique_to_sigs = {}
    len_5_sigs, len_6_sigs = set(), set()
    for num in in_sigs:
        sigs = frozenset(list(num))
        if len(sigs) in UNIQUE_SIGS_TO_NUM:
            unique_to_sigs[UNIQUE_SIGS_TO_NUM[len(sigs)]] = sigs

        elif len(sigs) == 5:
            len_5_sigs.add(sigs)

        else:
            len_6_sigs.add(sigs)

    one_sigs = unique_to_sigs[1]

    actual_a = get_elem_from_set(unique_to_sigs[7].difference(one_sigs))
    actual_to_orig[actual_a] = 'a'

    six_sigs = next(filter(lambda x: not one_sigs.issubset(x), len_6_sigs))
    len_6_sigs.remove(six_sigs)

    actual_f = get_elem_from_set(six_sigs.intersection(one_sigs))
    actual_to_orig[actual_f] = 'f'

    actual_c = get_elem_from_set(one_sigs.difference(one_sigs.intersection(six_sigs)))
    actual_to_orig[actual_c] = 'c'

    five_sigs = next(filter(lambda x: actual_c not in x, len_5_sigs))
    len_5_sigs.remove(five_sigs)

    opt1, opt2 = tuple(len_5_sigs)
    if one_sigs.issubset(opt1):
        three_sigs, two_sigs = opt1, opt2

    else:
        three_sigs, two_sigs = opt2, opt1

    actual_d = get_elem_from_set((unique_to_sigs[4].intersection(two_sigs)).difference(actual_c))
    actual_to_orig[actual_d] = 'd'

    opt1, opt2 = tuple(len_6_sigs)
    if actual_d in opt1:
        nine_sigs, zero_sigs = opt1, opt2

    else:
        nine_sigs, zero_sigs = opt2, opt1

    actual_g = get_elem_from_set(three_sigs.difference(actual_to_orig))
    actual_to_orig[actual_g] = 'g'

    actual_b = get_elem_from_set(nine_sigs.difference(actual_to_orig))
    actual_to_orig[actual_b] = 'b'

    actual_e = get_elem_from_set(zero_sigs.difference(actual_to_orig))
    actual_to_orig[actual_e] = 'e'

    return actual_to_orig


def decode_sig(sig: str, mapping: dict[str, str]) -> int:
    orig_sigs = [mapping[x] for x in sig]
    return SIGS_TO_NUM[frozenset(orig_sigs)]


def compute_row(row: Row) -> int:
    in_sigs, out_sigs = row
    mapping = decode(in_sigs)

    res = 0
    for sig in out_sigs:
        res *= 10
        res += decode_sig(sig, mapping)

    return res


def part2(data: Data) -> int:
    return sum(map(lambda x: compute_row(x), data))


if __name__ == '__main__':
    aoc = AoC(day=8, parse_fn=parse, part1_fn=part1, part2_fn=part2)

    example_data = parse_example()
    # aoc.solve(example_data)

    aoc.solve()
    aoc.submit()

