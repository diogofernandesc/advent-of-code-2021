def _calculate_commonality(no_of_zeros, length):
    if length - no_of_zeros > no_of_zeros:
        return "1"

    return "0"


def part1():
    # Track the number of zeros
    numbers = {}
    length = 0
    with open("input.txt") as f:
        for line_of_digits in f:
            length += 1
            line_of_digits = list(line_of_digits.strip())

            # Track the number of zeros across each column of digits
            for idx, val in enumerate(line_of_digits):
                if int(val) == 0:
                    if idx not in numbers:
                        numbers[idx] = 0
                    numbers[idx] = numbers[idx] + 1

        gamma_rate = [0 for i in range(0, len(numbers.keys()))]

        for idx, zero_count in numbers.items():
            gamma_rate[idx] = _calculate_commonality(zero_count, length)

        # Invert gamma rate
        epsilon_rate = ''.join('1' if x == '0' else '0' for x in gamma_rate)

        gamma_rate = int("".join(gamma_rate), 2)
        epsilon_rate = int(epsilon_rate, 2)
        return gamma_rate * epsilon_rate


def _get_commonality_at_index(numbers_list, index, inverse=False):
    no_of_zeros = 0
    no_of_1s = 0

    zero_indexes = []
    one_indexes = []
    count = 0
    for binary_number in numbers_list:
        val = binary_number[index]
        if int(val) == 0:
            no_of_zeros += 1
            zero_indexes.append(count)
        else:
            no_of_1s += 1
            one_indexes.append(count)
        count += 1

    if inverse:
        if no_of_zeros > no_of_1s:
            return one_indexes
        return zero_indexes

    if no_of_zeros > no_of_1s:
        return zero_indexes

    return one_indexes


def part2():
    oxygen_numbers = []
    co2_numbers = []
    with open("input.txt") as f:
        f.seek(0)
        for line_of_digits in f:
            oxygen_numbers.append(line_of_digits.strip())
            co2_numbers.append(line_of_digits.strip())

    i = 0
    while len(oxygen_numbers) > 1:
        dominant_indexes = _get_commonality_at_index(oxygen_numbers, i)
        oxygen_numbers = [oxygen_numbers[x] for x in dominant_indexes]
        i += 1

    oxygen_rating = oxygen_numbers[0]

    i = 0
    while len(co2_numbers) > 1:
        dominant_indexes = _get_commonality_at_index(co2_numbers, i, inverse=True)
        co2_numbers = [co2_numbers[x] for x in dominant_indexes]
        i += 1

    co2_rating = co2_numbers[0]

    return int(oxygen_rating, 2) * int(co2_rating, 2)


if __name__ == '__main__':
    print(part1())
    print(part2())