from pathlib import Path


def part_one(puzzle_input):
    dx, dy = 0, 0
    for instruction in puzzle_input:
        pos, value = instruction
        if pos == 'forward':
            dx += value
        elif pos == 'up':
            dy -= value
        else:
            dy += value
    return dx*dy


def part_two(puzzle_input):
    dx, dy, aim = 0, 0, 0
    for instruction in puzzle_input:
        pos, value = instruction
        if pos == 'forward':
            dx += value
            dy += aim*value
        elif pos == 'up':
            aim -= value
        else:
            aim += value
    return dx*dy


if __name__ == '__main__':
    puzzle_input = [i.split() for i in Path('input.txt').read_text().splitlines()]
    puzzle_input = [(i[0], int(i[1])) for i in puzzle_input]
    print(f'Part one: {part_one(puzzle_input)}')
    print(f'Part two: {part_two(puzzle_input)}')
