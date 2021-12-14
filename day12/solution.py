from collections import defaultdict

from utils import AoC

Data = list[list[str]]

START_NODE = 'start'

END_NODE = 'end'

class Graph:
    def __init__(self, edges: Data):
        self.graph = defaultdict(set)
        for [s, e] in edges:
            self.graph[s].add(e)
            self.graph[e].add(s)

    def get_num_path(self, s: str, e: str) -> int:
        return self._find_paths(s, e, set(self.graph.keys()))

    def _find_paths(self, s: str, e: str, nodes: set[str]) -> int:
        if s == e:
            return 1

        if not s.isupper():
            nodes = nodes.difference((s,))

        return sum((self._find_paths(n, e, nodes) for n in self.graph[s] if n in nodes))

    def get_special_num_path(self, s: str, e: str) -> int:
        return self._find_special_paths(s, e, set(self.graph.keys()), True)

    def _find_special_paths(self, s: str, e: str, nodes: set[str], has_life: bool) -> int:
        if s == e:
            return 1

        if not s.isupper():
            nodes = nodes.difference((s,))

        paths = 0
        if has_life:
            paths += sum((self._find_special_paths(n, e, nodes, False) for n in self.graph[s] if n not in nodes.union((START_NODE, END_NODE))))

        paths += sum((self._find_special_paths(n, e, nodes, has_life) for n in self.graph[s] if n in nodes))
        return paths

    def __repr__(self):
        return f"Graph({repr(self.graph)}"


def parse(string: str) -> Graph:
    return Graph([line.split('-') for line in string.splitlines()])


def part1(data: Graph) -> int:
    return data.get_num_path(START_NODE, END_NODE)


def part2(data: Graph) -> int:
    return data.get_special_num_path(START_NODE, END_NODE)


if __name__ == '__main__':
    aoc = AoC(day=12, parse_fn=parse, part1_fn=part1, part2_fn=part2)

    aoc.solve()
    aoc.submit()

#     example_data_1 = parse("""start-A
# start-b
# A-c
# A-b
# b-d
# A-end
# b-end""")
#
#     aoc.solve(example_data_1)
#
#     example_data_2 = parse("""dc-end
# HN-start
# start-kj
# dc-start
# dc-HN
# LN-dc
# HN-end
# kj-sa
# kj-HN
# kj-dc""")
#
#     aoc.solve(example_data_2)
#
#     example_data_3 = parse("""fs-end
# he-DX
# fs-he
# start-DX
# pj-DX
# end-zg
# zg-sl
# zg-pj
# pj-he
# RW-he
# fs-DX
# pj-RW
# zg-RW
# start-pj
# he-WI
# zg-he
# pj-fs
# start-RW""")
#     aoc.solve(example_data_3)
