constraints = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def get_input() -> list[str]:
    with open('2023/day2/input.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines

def part1():
    valid_games = []

    lines = get_input()
    for line in lines:
        game_number_str, hands = line.split(":")
        game_number = game_number_str.split()[1]
        hands = ", ".join([hand.strip() for hand in hands.split(";")])
        hands = [h.split() for h in hands.split(',')]
        is_valid = all([int(roll[0]) <= constraints[roll[1]] for roll in hands])
        if is_valid:
            valid_games.append(int(game_number))

    return sum(valid_games)

def part2():
    lines = get_input()
    powers = []
    for line in lines:
        _, hands = line.split(":")
        hands = ", ".join([hand.strip() for hand in hands.split(";")])
        hands = [h.split() for h in hands.split(',')]

        mins = {
            'red': 0,
            'blue': 0,
            'green': 0
        }

        for roll in hands:
            num, color = roll
            if int(num) > mins[color]:
                mins[color] = int(num)

        powers.append(mins['blue'] * mins['green'] * mins['red'])

    return sum(powers)

if __name__ == "__main__":
    print(part1())
    print(part2())