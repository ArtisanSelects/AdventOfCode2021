from pathlib import Path
from collections import namedtuple
from bisect import insort
from math import prod


def solve_puzzle(puzzle_input):

    def get_low_points(puzzle_input):
        res = []
        for y in range(max_y):
            for x in range(max_x):
                height = puzzle_input[y][x]
                is_valid = True
                adjacent = get_adjacent_coords(x, y)
                for i in adjacent:
                    dx, dy = i
                    if coord_in_range(dx, dy) and puzzle_input[dy][dx] <= height:
                        is_valid = False
                        break
                if is_valid:
                    res.append(Coord(x, y, height))
        return res

    def get_adjacent_coords(x, y):
        return [(x+i[0], y+i[1]) for i in adjacent_modifiers]

    def coord_in_range(x, y):
        return 0 <= x < max_x and 0 <= y < max_y

    adjacent_modifiers = set([(-1, 0), (0, -1), (1, 0), (0, 1)])
    max_x = len(puzzle_input[0])
    max_y = len(puzzle_input)
    Coord = namedtuple('Coord', 'x y height')
    low_points = get_low_points(puzzle_input)
    basins = []
    in_basins = set()
    for low_point in low_points:
        basin = []
        to_check = [low_point]
        while len(to_check) > 0:
            checking = to_check.pop()
            if checking in in_basins:
                continue
            basin.append(checking)
            in_basins.add(checking)
            adjacent = get_adjacent_coords(checking.x, checking.y)
            for i in adjacent:
                if coord_in_range(i[0], i[1]):
                    new_point = Coord(i[0], i[1], puzzle_input[i[1]][i[0]])
                    if new_point.height < 9 and checking.height < new_point.height:
                        to_check.append(new_point)
        insort(basins, len(basin))
    return [sum([i.height+1 for i in low_points]), prod(basins[-3:])]


if __name__ == '__main__':
    puzzle_input = [list(map(int, list(i))) for i in Path('input.txt').read_text().splitlines()]
    part_one, part_two = solve_puzzle(puzzle_input)
    print(f'Part one: {part_one}')
    print(f'Part two: {part_two}')
