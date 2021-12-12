from pathlib import Path
from collections import defaultdict


def solve_puzzle(puzzle_input):

    def valid_path(path, cave, part_one=False):
        if cave in small_caves and cave in path:
            if part_one:
                return False
            path_caves = [i for i in path if i in small_caves]
            if len(path_caves) != len(set(path_caves)):
                return False
        return True

    def find_paths(part_one=False):
        res = 0
        to_check = [['start']]
        while len(to_check) > 0:
            path = to_check.pop()
            connections = caves[path[-1]]
            for i in connections:
                if i == 'end':
                    res += 1
                elif valid_path(path, i, part_one):
                    to_check.append(path+[i])
        return res

    caves = defaultdict(list)
    for i in puzzle_input:
        caves[i[0]].append(i[1])
        caves[i[1]].append(i[0])
    for k, v in caves.items():
        caves[k] = [i for i in v if i != 'start']
    small_caves = set([i for i in caves.keys() if
                       ord(i[0]) >= 97 and i not in {'start', 'end'}])
    part_one = find_paths(True)
    part_two = find_paths()
    return part_one, part_two


if __name__ == '__main__':
    puzzle_input = [i.split('-') for i in
                    Path('input.txt').read_text().splitlines()]
    part_one, part_two = solve_puzzle(puzzle_input)
    print(f'Part one: {part_one}')
    print(f'Part two: {part_two}')
