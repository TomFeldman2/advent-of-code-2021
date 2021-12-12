INPUT_FILE = "input.txt"


def get_input() -> list[str]:
    with open(INPUT_FILE) as f:
        return f.readlines()


def part1_main():
    horizon, depth = 0, 0

    action = {
        "forward": lambda x: (horizon + x, depth),
        "up": lambda x: (horizon, depth - x),
        "down": lambda x: (horizon, depth + x),
    }

    for line in get_input():
        direction, size = line.split(' ')
        horizon, depth = action[direction](int(size))

    return horizon * depth

def part2_main():
    horizon, depth, aim = 0, 0, 0

    action = {
        "forward": lambda x: (horizon + x, depth + x*aim, aim),
        "up": lambda x: (horizon, depth, aim - x),
        "down": lambda x: (horizon, depth, aim + x),
    }

    for line in get_input():
        direction, size = line.split(' ')
        horizon, depth, aim = action[direction](int(size))

    return horizon * depth

if __name__ == '__main__':
    print(part2_main())
