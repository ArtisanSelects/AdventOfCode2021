from pathlib import Path
from collections import deque


def count_lanternfish(puzzle_input, days):
    fish = deque([0 for _ in range(9)], 9)
    for i in puzzle_input:
        fish[i] += 1
    for _ in range(days):
        new_fish = fish.popleft()
        fish[6] += new_fish
        fish.append(new_fish)
    return sum(fish)


if __name__ == '__main__':
    puzzle_input = [int(i) for i in Path('input.txt').read_text().split(',')]
    print(f'Part one: {count_lanternfish(puzzle_input, 80)}')
    print(f'Part two: {count_lanternfish(puzzle_input, 256)}')
