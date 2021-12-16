from pathlib import Path
import heapq


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.cost = 0
        self.wcost = 0

    def __lt__(self, other):
        return self.wcost < other.wcost


def solve_puzzle(puzzle_input):

    def get_valid_coords(x, y):
        res = set()
        all_coords = {(x+i[0], y+i[1]) for i in adjacent_modifiers}
        for i in all_coords:
            if 0 <= i[0] < max_len and 0 <= i[1] < max_len:
                res.add(i)
        return res

    def heuristic(current_node):
        x1, y1 = current_node
        x2, y2 = end_node_position
        return abs(x1-x2)+abs(y1-y2)

    def get_path_cost(end_node):
        res = 0
        node = end_node
        while node.parent:
            res += costs[node.position]
            node = node.parent
        return res

    adjacent_modifiers = {(0, 1), (0, -1), (1, 0), (-1, 0)}
    max_len = len(puzzle_input)
    end_node_position = (max_len-1, max_len-1)
    start_node = Node((0, 0))

    nodes = {(x, y) for x in range(max_len) for y in range(max_len)}
    connections = {i: get_valid_coords(i[0], i[1]) for i in nodes}
    costs = {i: puzzle_input[i[1]][i[0]] for i in nodes}

    processing = []
    resolved = set()
    heapq.heapify(processing)
    heapq.heappush(processing, start_node)

    while processing:
        min_node = heapq.heappop(processing)
        resolved.add(min_node.position)
        if min_node.position == end_node_position:
            return get_path_cost(min_node)
        for connection in connections[min_node.position]:
            if connection in resolved:
                continue
            connection = Node(connection, min_node)
            connection.cost = min_node.cost+costs[connection.position]
            connection.wcost = connection.cost+heuristic(connection.position)
            if not [i for i in processing if
                    i.position == connection.position and
                    i.cost < connection.cost]:
                heapq.heappush(processing, connection)


def extend_grid(puzzle_input, amount):
    original_len = len(puzzle_input)
    new_len = original_len*amount
    res = [i for i in puzzle_input]

    for y in range(original_len):
        row = res[y]
        for x in range(original_len, new_len):
            new_value = res[y][x-original_len]+1
            if new_value > 9:
                new_value -= 9
            row.append(new_value)
        res[y] = tuple(row)

    for y in range(original_len, new_len):
        row = [i for i in res[y-original_len]]
        for x in range(new_len):
            new_value = row[x]+1
            if new_value > 9:
                new_value -= 9
            row[x] = new_value
        res.append(row)

    return tuple(res)


if __name__ == '__main__':
    puzzle_input = [list(map(int, list(i))) for i in
                    Path('input.txt').read_text().splitlines()]
    part_two = extend_grid(puzzle_input, 5)
    print(f'Part one: {solve_puzzle(puzzle_input)}')
    print(f'Part two: {solve_puzzle(part_two)}')
