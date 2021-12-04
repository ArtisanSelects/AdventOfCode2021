from pathlib import Path


class BingoCard:
    def __init__(self, rows):
        self.rows = rows
        self.winning_combinations = self.generate_winning_combinations()
        self.all_numbers = self.generate_all_numbers()

    def generate_winning_combinations(self):
        res = []
        board_size = len(self.rows)
        rows = [set(i) for i in self.rows]
        columns = [set() for _ in range(board_size)]
        for y in range(board_size):
            for x in range(board_size):
                columns[x].add(self.rows[y][x])
        return rows+columns

    def generate_all_numbers(self):
        res = set()
        for i in self.rows:
            res.update(i)
        return res

    def check_winning_combinations(self, called_numbers):
        for i in self.winning_combinations:
            if len(i-called_numbers) == 0:
                return True
        return False

    def get_puzzle_solution(self, called_numbers, last_number):
        return sum(self.all_numbers-called_numbers)*last_number


def generate_bingo_cards(puzzle_input):
    cards = [i for i in puzzle_input[1:] if i != '']
    current_row = []
    bingo_cards = []
    for i in cards:
        current_row.append([int(j) for j in i.split()])
        if len(current_row) == 5:
            bingo_cards.append(BingoCard(current_row))
            current_row = []
    return bingo_cards


def part_one(bingo_cards, numbers):
    called_numbers = set()
    for number in numbers:
        called_numbers.add(number)
        for card in bingo_cards:
            if card.check_winning_combinations(called_numbers):
                return card.get_puzzle_solution(called_numbers, number)


def part_two(bingo_cards, numbers):
    bingo_cards = set(bingo_cards)
    called_numbers = set()
    winning_cards = set()
    for number in numbers:
        called_numbers.add(number)
        for card in bingo_cards:
            if card.check_winning_combinations(called_numbers):
                winning_cards.add(card)
                latest_winner = card
        if len(bingo_cards) == 1:
            return latest_winner.get_puzzle_solution(called_numbers, number)
        bingo_cards -= winning_cards


if __name__ == '__main__':
    puzzle_input = Path('input.txt').read_text().splitlines()
    numbers = [int(i) for i in puzzle_input[0].split(',')]
    bingo_cards = generate_bingo_cards(puzzle_input)
    print(f'Part one: {part_one(bingo_cards, numbers)}')
    print(f'Part two: {part_two(bingo_cards, numbers)}')
