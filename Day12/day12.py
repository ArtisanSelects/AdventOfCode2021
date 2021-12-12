from pathlib import Path
from collections import defaultdict


def solve_puzzle(puzzle_input):

    def is_small_cave(cave):
        return ord(cave[0]) >= 97

    def valid_path_part_one(path, cave):
        if is_small_cave(cave) and cave in path:
            return False
        return True

    def valid_path_part_two(path, cave):
        if is_small_cave(cave) and cave in path:
            small_caves = [i for i in path if is_small_cave(i)]
            if len(small_caves) != len(set(small_caves)):
                return False
        return True

    def find_paths(part_one=False):
        res = []
        to_check = [['start']]
        processor = valid_path_part_one if part_one else valid_path_part_two
        while len(to_check) > 0:
            path = to_check.pop()
            connections = caves[path[-1]]
            for i in connections:
                if i == 'end':
                    res.append(path+['end'])
                elif processor(path, i):
                    to_check.append(path+[i])
        return len(res)

    caves = defaultdict(list)
    for i in puzzle_input:
        caves[i[0]].append(i[1])
        caves[i[1]].append(i[0])
    for k, v in caves.items():
        caves[k] = [i for i in v if i != 'start']
    part_one = find_paths(True)
    part_two = find_paths()
    return part_one, part_two

if __name__ == '__main__':
    puzzle_input = [i.split('-') for i in
                    Path('input.txt').read_text().splitlines()]
    part_one, part_two = solve_puzzle(puzzle_input)
    print(f'Part one: {part_one}')
    print(f'Part two: {part_two}')
