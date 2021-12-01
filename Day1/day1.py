from pathlib import Path


def part_one(puzzle_input):
    res = 0
    for i in range(1, len(puzzle_input)):
        res += puzzle_input[i] > puzzle_input[i-1]
    return res


def part_two(puzzle_input):
    res = 0
    for i in range(len(puzzle_input)-3):
        res += sum(puzzle_input[i+1:i+4]) > sum(puzzle_input[i:i+3])
    return res


if __name__ == '__main__':
    puzzle_input = [int(i) for i in Path('input.txt').read_text().splitlines()]
    print(f'Part one: {part_one(puzzle_input)}')
    print(f'Part two: {part_two(puzzle_input)}')
