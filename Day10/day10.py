from pathlib import Path
from bisect import insort


def solve_puzzle(puzzle_input):
    bracket_pairs = {'(': ')',
                     '[': ']',
                     '{': '}',
                     '<': '>'}
    opening_brackets = bracket_pairs.keys()
    values = {')': 3, ']': 57, '}': 1197, '>': 25137,
              '(': 1, '[': 2, '{': 3, '<': 4}
    part_one = 0
    part_two = []
    for line in puzzle_input:
        brackets = []
        for bracket in line:
            is_valid = True
            if bracket in opening_brackets:
                brackets.append(bracket)
            else:
                if bracket_pairs[brackets.pop()] != bracket:
                    part_one += values[bracket]
                    is_valid = False
                    break
        if is_valid:
            score = 0
            for bracket in reversed(brackets):
                score = (score*5)+values[bracket]
            insort(part_two, score)
    return part_one, part_two[len(part_two)//2]


if __name__ == '__main__':
    puzzle_input = Path('input.txt').read_text().splitlines()
    part_one, part_two = solve_puzzle(puzzle_input)
    print(f'Part one: {part_one}')
    print(f'Part two: {part_two}')
