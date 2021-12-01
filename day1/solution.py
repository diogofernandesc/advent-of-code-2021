def part1():
    count = 0
    with open("input.txt") as f:
        last_reading = int(f.readline())
        for new_reading in f:
            new_reading = int(new_reading)
            if new_reading > last_reading:
                count += 1

            last_reading = new_reading

    return count


def part2():
    count = 0
    with open("input.txt") as f:
        readings = [int(r) for r in f.read().splitlines()]

    last_window = sum(readings[0:3])
    for idx in range(1, len(readings)):
        new_window = sum(readings[idx:idx+3])
        if new_window > last_window:
            count += 1

        last_window = new_window

    return count


if __name__ == '__main__':
    part1()
    part2()