def get_input():
    with open('2023/day4/input.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines

def part1():
    lines = get_input()

    points = 0

    for line in lines:
        game_points = 0
        game, player_numbers = line.split('|')
        game_numbers = [j.split(" ") for j in game.split(":")[1].strip().split('  ')]
        game_numbers = [int(i) for l in game_numbers for i in l]

        player_numbers = [j.split(" ") for j in player_numbers.strip().split("  ")]
        player_numbers = [int(i) for l in player_numbers for i in l]

        for player_num in player_numbers:
            if player_num in game_numbers:
                if game_points == 0:
                    game_points = 1
                else:
                    game_points *= 2
        points += game_points
    
    print(points)



def part2():
    lines = get_input()

    copies = dict()

    cards_played = 0

    for card_number, line in enumerate(lines):
        card_number = card_number + 1
        next_card_number = card_number + 1
        game, player_numbers = line.split('|')
        game_numbers = [j.split(" ") for j in game.split(":")[1].strip().split('  ')]
        game_numbers = [int(i) for l in game_numbers for i in l]

        player_numbers = [j.split(" ") for j in player_numbers.strip().split("  ")]
        player_numbers = [int(i) for l in player_numbers for i in l]

        copies_to_play = copies.get(card_number, 0)
        number_of_matches = 0

        for player_num in player_numbers:
            if player_num in game_numbers: # this is a match
                number_of_matches += 1
        
        # get ticket copies from this card
        for i in range(next_card_number, next_card_number+number_of_matches):
            if not i in copies:
                copies[i] = 1
            else:
                copies[i] += 1

        # play the copies
        for _ in range(copies_to_play):
            for i in range(next_card_number, next_card_number+number_of_matches):
                if not i in copies:
                    copies[i] = 1
                else:
                    copies[i] += 1

        cards_played += 1      
    print(sum(copies.values()) + cards_played)



if __name__ == "__main__":
    part1()
    part2()
