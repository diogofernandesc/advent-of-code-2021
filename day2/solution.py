def part1():
    horizontal, depth = 0, 0
    depth_moves = {
        "down": lambda x: int(x),
        "up": lambda x: -(int(x))
    }

    horizontal_moves = {
        "forward": lambda x: int(x),
    }

    with open("input.txt") as f:
        for command in f:
            move, scalar = command.split(" ")
            depth += depth_moves.get(move, lambda x: 0)(scalar)
            horizontal += horizontal_moves.get(move, lambda x: 0)(scalar)

    return horizontal * depth


def part2():
    horizontal, depth, aim = 0, 0, 0
    depth_moves = {
        "down": lambda x: int(x),
        "up": lambda x: -(int(x))
    }

    horizontal_moves = {
        "forward": lambda x: int(x),
    }
    with open("input.txt") as f:
        for command in f:
            move, scalar = command.split(" ")
            move_horizontally = horizontal_moves.get(move, lambda x: 0)
            move_vertically = depth_moves.get(move, lambda x: 0)

            aim += move_vertically(scalar)
            depth += aim * move_horizontally(scalar)
            horizontal += move_horizontally(scalar)

    return horizontal * depth


if __name__ == '__main__':
    print(part1())
    print(part2())