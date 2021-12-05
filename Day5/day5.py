from pathlib import Path
from collections import defaultdict


class Coord:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.all_positions = self.generate_all_positions()

    def generate_all_positions(self):
        res = set()
        step_x, step_y = 0, 0
        if self.x1 > self.x2:
            step_x = -1
        elif self.x1 < self.x2:
            step_x = 1
        if self.y1 > self.y2:
            step_y = -1
        elif self.y1 < self.y2:
            step_y = 1
        line_len = max(abs(self.x2-self.x1), abs(self.y2-self.y1))
        for i in range(line_len+1):
            res.add((self.x1+(i*step_x), self.y1+(i*step_y)))
        return res


def solve_puzzle(puzzle_input, part_one=False):
    valid_coords = []
    for coord in puzzle_input:
        coords = [i.split(',') for i in coord]
        x1, y1 = [int(i) for i in coords[0]]
        x2, y2 = [int(i) for i in coords[1]]
        if part_one and x1 != x2 and y1 != y2:
            continue
        valid_coords.append(Coord(x1, y1, x2, y2))
    res = defaultdict(int)
    for i in valid_coords:
        for coord in i.all_positions:
            res[coord] += 1
    return len([v for v in res.values() if v > 1])


if __name__ == '__main__':
    puzzle_input = Path('input.txt').read_text().splitlines()
    puzzle_input = [i.split(' -> ') for i in puzzle_input]
    print(f'Part one: {solve_puzzle(puzzle_input, True)}')
    print(f'Part two: {solve_puzzle(puzzle_input)}')
