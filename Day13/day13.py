from pathlib import Path


def format_puzzle_input(puzzle_input):
    res = [[], []]
    split_point = puzzle_input.index('')
    res[0] = [list(map(int, i.split(','))) for i in puzzle_input[:split_point]]
    for i in puzzle_input[split_point+1:]:
        axis, coord = i.split('=')
        res[1].append((axis[-1] == 'y', int(coord)))
    return res


def solve_puzzle(puzzle_input):

    def fold_page(axis, fold):
        for coord in coords:
            if coord[axis] > fold:
                coord[axis] = fold-(coord[axis]-fold)

    coords, instructions = puzzle_input
    fold_page(instructions[0][0], instructions[0][1])
    part_one = len(set([(i[0], i[1]) for i in coords]))
    for axis, fold in instructions[1:]:
        fold_page(axis, fold)
    return part_one, coords


def print_coords(coords):
    y_range = max(i[1] for i in coords)+1
    x_range = max(i[0] for i in coords)+1
    grid = [['.' for _ in range(x_range)] for _ in range(y_range)]
    for x, y in coords:
        grid[y][x] = '#'
    for y in range(y_range):
        print(''.join(grid[y]))


if __name__ == '__main__':
    puzzle_input = Path('input.txt').read_text().splitlines()
    part_one, part_two = solve_puzzle(format_puzzle_input(puzzle_input))
    print(f'Part one: {part_one}')
    print(f'Part two: \n')
    print_coords(part_two)
