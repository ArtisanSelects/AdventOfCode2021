from pathlib import Path
from collections import defaultdict


def part_one(puzzle_input):
    unique_segments = set([7, 2, 4, 3])
    res = 0
    for i in puzzle_input:
        for output in i[1]:
            res += len(output) in unique_segments
    return res


def part_two(puzzle_input):
    # b, e, and f have a unique frequency in the groups
    #   (b = 6/10 groups, e = 4/10, f = 9/10)
    # c is the letter in the group of length 2 that isn't f
    # d is the letter in the group of length 4 that isn't b, c, or f
    # a is the letter in the group of length 3 that isn't c or f
    # g is found via process of elimination

    res = 0
    numbers_dict = dict()
    numbers = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
    for i in range(len(numbers)):
        numbers_dict[numbers[i]] = i
    for i in puzzle_input:
        letter_maps, output = i
        scrambled_letters = dict()
        scrambled_letters_freq = defaultdict(int)
        for code in letter_maps:
            for letter in code:
                scrambled_letters_freq[letter] += 1
        one, seven, four = sorted([i for i in letter_maps if len(i) in (2, 4, 3)], key=lambda x: len(x))
        unique_frequencies = {v: k for k, v in scrambled_letters_freq.items() if v in {6, 4, 9}}
        scrambled_letters['b'] = unique_frequencies[6]
        scrambled_letters['e'] = unique_frequencies[4]
        scrambled_letters['f'] = unique_frequencies[9]
        scrambled_letters['c'] = one.replace(scrambled_letters['f'], '')
        scrambled_letters['d'] = [i for i in four if i not in scrambled_letters.values()][0]
        scrambled_letters['a'] = [i for i in seven if i not in scrambled_letters.values()][0]
        scrambled_letters['g'] = [i for i in 'abcdefg' if i not in scrambled_letters.values()][0]
        true_letters = {v: k for k, v in scrambled_letters.items()}
        output_int = ''
        for i in output:
            output_int += str(numbers_dict[''.join(sorted([true_letters[j] for j in i]))])
        res += int(output_int)
    return res


if __name__ == '__main__':
    puzzle_input = [i.split(' | ') for i in Path('input.txt').read_text().splitlines()]
    puzzle_input = [[i[0].split(), i[1].split()] for i in puzzle_input]
    print(f'Part one: {part_one(puzzle_input)}')
    print(f'Part two: {part_two(puzzle_input)}')
