from pathlib import Path


def solve_puzzle(puzzle_input):

    class Probe:
        def __init__(self, velocity, targets):
            self.x = 0
            self.y = 0
            self.max_height = 0
            self.xvel = velocity[0]
            self.yvel = velocity[1]
            self.x_min = targets['x_min']
            self.y_min = targets['y_min']
            self.x_max = targets['x_max']
            self.y_max = targets['y_max']

        def in_range(self):
            return (self.x_min <= self.x <= self.x_max and
                    self.y_min <= self.y <= self.y_max)

        def has_failed(self):
            if ((self.x > self.x_max) or
                    (self.x < self.x_min and self.xvel == 0) or
                    (self.y < self.y_min and self.x > self.x_min)):
                return True
            return False

        def perform_step(self):
            self.x += self.xvel
            self.y += self.yvel
            if self.xvel != 0:
                self.xvel = self.xvel+1 if self.xvel < 0 else self.xvel-1
            self.yvel -= 1
            self.max_height = max(self.y, self.max_height)

        def validate_self(self):
            while not self.has_failed():
                self.perform_step()
                if self.in_range():
                    return (True, self.max_height)
            return (False, 0)

    x_range, y_range = puzzle_input.split(', y=')
    x_range = tuple(map(int, x_range.split('..')))
    y_range = tuple(map(int, y_range.split('..')))
    targets = {'x_min': min(x_range), 'x_max': max(x_range),
               'y_min': min(y_range), 'y_max': max(y_range)}
    part_one, part_two = (0, 0)

    for xvel in range(targets['x_max']+1):
        for yvel in range(-abs(targets['y_min']), abs(targets['y_min'])):
            success, max_y = Probe([xvel, yvel], targets).validate_self()
            part_one = max(part_one, max_y)
            part_two += success

    return part_one, part_two


if __name__ == '__main__':
    puzzle_input = Path('input.txt').read_text()[15:]
    part_one, part_two = solve_puzzle(puzzle_input)
    print(f'Part one: {part_one}')
    print(f'Part two: {part_two}')
