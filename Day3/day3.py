from pathlib import Path


def part_one(puzzle_input):
    bit_counts = dict()
    binary_length = len(puzzle_input[0])
    for i in range(binary_length):
        bit_counts[i] = {'0': 0, '1': 0}
    for i in puzzle_input:
        for j in range(binary_length):
            bit_counts[j][i[j]] += 1
    gamma_rate = ''
    for k, v in bit_counts.items():
        gamma_rate += max(v.items(), key=lambda x: x[1])[0]
    epsilon_rate = ''.join(['0' if i == '1' else '1' for i in gamma_rate])
    return int(gamma_rate, 2)*int(epsilon_rate, 2)


def part_two(puzzle_input):

    def bit_criteria(puzzle_input, oxygen_check=True):
        bit_position = -1
        while len(puzzle_input) > 1:
            bit_counts = {'0': 0, '1': 0}
            bit_position += 1
            for i in puzzle_input:
                bit_counts[i[bit_position]] += 1
            if oxygen_check:
                if bit_counts['1'] >= bit_counts['0']:
                    wanted_bit = '1'
                else:
                    wanted_bit = '0'
            else:
                if bit_counts['0'] <= bit_counts['1']:
                    wanted_bit = '0'
                else:
                    wanted_bit = '1'
            puzzle_input = [i for i in puzzle_input if i[bit_position] == wanted_bit]
        return puzzle_input[0]

    oxygen_rating = bit_criteria(puzzle_input)
    co2_rating = bit_criteria(puzzle_input, False)
    return int(oxygen_rating, 2)*int(co2_rating, 2)


if __name__ == '__main__':
    puzzle_input = Path('input.txt').read_text().splitlines()
    print(f'Part one: {part_one(puzzle_input)}')
    print(f'Part two: {part_two(puzzle_input)}')
