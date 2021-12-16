import functools

from utils import AoC

Data = str

HEX_TO_BIN = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


def bin_to_dec(bin_str: str) -> int:
    val = 0
    for c in bin_str:
        val <<= 1
        val += 0 if c == '0' else 1

    return val


def to_binary(hex_str: str) -> str:
    return ''.join([HEX_TO_BIN[c] for c in hex_str])


def parse(string: str) -> Data:
    return to_binary(string)


def parse_packet(packet: str) -> tuple[tuple[int, int], str]:
    version = bin_to_dec(packet[:3])
    type_id = bin_to_dec(packet[3:6])

    if type_id == 4:
        value, packet = parse_literal(packet[6:])

    else:
        (versions, value), packet = parse_sub_packet(packet[6:], type_id)
        version += versions

    return (version, value), packet


def parse_literal(packet: str) -> tuple[int, str]:
    bin_num = ""

    i = None
    for i in range(0, len(packet), 5):
        bin_num += packet[i + 1: i + 5]
        if packet[i] == '0':
            break

    return bin_to_dec(bin_num), packet[i + 5:]


def parse_sub_packet(packet: str, type_id: int) -> tuple[tuple[int, int], str]:
    cnt, versions = 0, 0

    values = []

    if packet[0] == '0':
        sub_packets_len = bin_to_dec(packet[1:1 + 15])
        packet = packet[16:]
        while cnt < sub_packets_len:
            (version, value), rest = parse_packet(packet)
            values.append(value)
            versions += version
            cnt += (len(packet) - len(rest))
            packet = rest

    else:
        sub_packets_num = bin_to_dec(packet[1:1 + 11])
        packet = packet[12:]
        for _ in range(sub_packets_num):
            (version, value), packet = parse_packet(packet)
            values.append(value)
            versions += version

    final_value = None
    assert type_id != 4
    if type_id == 0:
        final_value = sum(values)
    elif type_id == 1:
        final_value = functools.reduce(lambda x, y: x * y, values)
    elif type_id == 2:
        final_value = min(values)
    elif type_id == 3:
        final_value = max(values)
    elif type_id == 5:
        assert len(values) == 2
        final_value = int(values[0] > values[1])
    elif type_id == 6:
        assert len(values) == 2
        final_value = int(values[1] > values[0])
    elif type_id == 7:
        assert len(values) == 2
        final_value = int(values[0] == values[1])

    return (versions, final_value), packet


def part1(data: Data) -> int:
    return parse_packet(data)[0][0]


def part2(data: Data) -> int:
    return parse_packet(data)[0][1]


if __name__ == '__main__':
    aoc = AoC(day=16, parse_fn=parse, part1_fn=part1, part2_fn=part2)

    # aoc.solve(parse("CE00C43D881120"))

    aoc.solve()
    aoc.submit()
