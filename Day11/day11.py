from pathlib import Path


class Octo:
    def __init__(self, energy, x, y):
        self.energy = energy
        self.x = x
        self.y = y

    def process(self):
        if self.energy > 9:
            return False
        self.energy += 1
        return self.energy > 9

    def handle_reset(self):
        if self.energy > 9:
            self.energy = 0
            return True
        return False


def solve_puzzle(puzzle_input):

    def generate_octos():
        for y in range(max_y):
            row = []
            for x in range(max_x):
                row.append(Octo(puzzle_input[y][x], x, y))
            octos.append(row)

    def get_valid_coords(x, y):
        all_coords = [(x+i[0], y+i[1]) for i in adjacent_modifiers]
        return [i for i in all_coords if
                0 <= i[0] < max_x and 0 <= i[1] < max_y]

    def handle_flash(octo):
        flashed = []
        adjacent_octos = get_valid_coords(octo.x, octo.y)
        for i in adjacent_octos:
            if octos[i[1]][i[0]].process():
                flashed.append(octos[i[1]][i[0]])
        return flashed

    def run_step():
        res = 0
        flashed = []
        for y in range(max_y):
            for x in range(max_x):
                if octos[y][x].process():
                    flashed.append(octos[y][x])
        while len(flashed) > 0:
            octo = flashed.pop()
            did_flash = handle_flash(octo)
            flashed += did_flash
        for y in range(max_y):
            for x in range(max_x):
                res += octos[y][x].handle_reset()
        return res

    part_one = 0
    part_two = 0
    octos = []
    adjacent_modifiers = set([(-1, 0), (0, -1), (1, 0), (0, 1),
                              (-1, -1), (1, 1), (1, -1), (-1, 1)])
    max_x = len(puzzle_input[0])
    max_y = len(puzzle_input)
    octo_count = max_x*max_y
    generate_octos()
    for _ in range(100):
        flash_count = run_step()
        if flash_count == octo_count:
            part_two = _
        part_one += flash_count
    if part_two > 0:
        return part_one, part_two
    part_two = 100
    while True:
        part_two += 1
        if run_step() == octo_count:
            return part_one, part_two


if __name__ == '__main__':
    puzzle_input = [list(map(int, list(i))) for i in
                    Path('input.txt').read_text().splitlines()]
    part_one, part_two = solve_puzzle(puzzle_input)
    print(f'Part one: {part_one}')
    print(f'Part two: {part_two}')
