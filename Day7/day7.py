from pathlib import Path
from collections import defaultdict


def solve_puzzle(puzzle_input, part_one=False):
    distances = set(range(min(puzzle_input), max(puzzle_input)+1))
    if part_one:
        distance_function = lambda x1, x2: abs(x1-x2)
    else:
        distance_function = lambda x1, x2: sum(range(abs(x1-x2)+1))
    sums = defaultdict(int)
    for crab in puzzle_input:
        for dist in distances:
            sums[dist] += distance_function(crab, dist)
    return min(sums.values())


if __name__ == '__main__':
    puzzle_input = [int(i) for i in Path('input.txt').read_text().split(',')]
    print(f'Part one: {solve_puzzle(puzzle_input, True)}')
    print(f'Part two: {solve_puzzle(puzzle_input)}')
