from pathlib import Path
from collections import defaultdict, Counter


def solve_puzzle(template, rules_list):

    def run_step():
        for k, v in res.copy().items():
            i, j = k
            new_char = rules[k]
            char_counts[new_char] += v
            res[k] -= v
            res[i+new_char] += v
            res[new_char+j] += v

    def solve_part():
        count_values = char_counts.values()
        return max(count_values)-min(count_values)

    rules = {i[0]: i[1] for i in rules_list}
    res = defaultdict(int)
    for i in range(len(template)-1):
        res[template[i:i+2]] += 1
    char_counts = Counter(template)
    for _ in range(10):
        run_step()
    part_one = solve_part()
    for _ in range(30):
        run_step()
    part_two = solve_part()
    return part_one, part_two


if __name__ == '__main__':
    puzzle_input = Path('input.txt').read_text().splitlines()
    template = puzzle_input[0]
    rules = [i.split(' -> ') for i in puzzle_input[2:]]
    part_one, part_two = solve_puzzle(template, rules)
    print(f'Part one: {part_one}')
    print(f'Part two: {part_two}')
