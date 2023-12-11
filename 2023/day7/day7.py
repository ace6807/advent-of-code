from enum import Enum, auto
from collections import Counter

def get_input():
    with open('2023/day7/input.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines

class Hand(Enum):
    FIVE_OF_A_KIND  = 7
    FOUR_OF_A_KIND  = 6
    FULL_HOUSE      = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR        = 3
    ONE_PAIR        = 2
    HIGH_CARD       = 1

class Card(Enum):
    ACE     = 13
    KING    = 12
    QUEEN   = 11
    JACK    = 10
    TEN     = 9
    NINE    = 8
    EIGHT   = 7
    SEVEN   = 6
    SIX     = 5
    FIVE    = 4
    FOUR    = 3
    THREE   = 2
    TWO     = 1
    JOKER   = 0

class HandComparison(Enum):
    HAND_1 = auto()
    HAND_2 = auto()
    TIE = auto()

def get_card_type(card: str, using_jokers=False) -> Card:
    match card, using_jokers:
        case 'A', _: return Card.ACE
        case 'K', _: return Card.KING
        case 'Q', _: return Card.QUEEN
        case 'J', using_jokers:
            if using_jokers:
                return Card.JOKER
            return Card.JACK
        case 'T', _: return Card.TEN
        case '9', _: return Card.NINE
        case '8', _: return Card.EIGHT
        case '7', _: return Card.SEVEN
        case '6', _: return Card.SIX
        case '5', _: return Card.FIVE
        case '4', _: return Card.FOUR
        case '3', _: return Card.THREE
        case '2', _: return Card.TWO

def get_hand_type(hand: str) -> Hand:
    counter = Counter(list(hand))
    dupes = counter.values()
    if 5 in dupes:
        return Hand.FIVE_OF_A_KIND
    if 4 in dupes:
        return Hand.FOUR_OF_A_KIND
    if 3 in dupes and 2 in dupes:
        return Hand.FULL_HOUSE
    if 3 in dupes:
        return Hand.THREE_OF_A_KIND
    if Counter(dupes)[2] == 2:
        return Hand.TWO_PAIR
    if 2 in dupes:
        return Hand.ONE_PAIR
    return Hand.HIGH_CARD

def get_hand_type_with_jokers(hand: str) -> Hand:
    counter = Counter(list(hand))

    jokers_counter = {'J': counter['J']}
    non_joker_counter = {k:v for k,v in counter.items() if k != 'J'}

    joker_count = jokers_counter['J']
    non_joker_counts = non_joker_counter.values()

    if 5 in non_joker_counts or joker_count == 5 or any([i + joker_count > 4 for i in non_joker_counts]):
        return Hand.FIVE_OF_A_KIND
    if 4 in non_joker_counts or joker_count == 4 or any([i + joker_count > 3 for i in non_joker_counts]):
        return Hand.FOUR_OF_A_KIND
    if (3 in non_joker_counts and 2 in non_joker_counts) or (Counter(non_joker_counts)[2] == 2 and joker_count == 1):
        return Hand.FULL_HOUSE
    if 3 in non_joker_counts or joker_count == 3 or any([i + joker_count > 2 for i in non_joker_counts]):
        return Hand.THREE_OF_A_KIND
    if Counter(non_joker_counts)[2] == 2:
        return Hand.TWO_PAIR
    if 2 in non_joker_counts or joker_count == 2 or any([i + joker_count > 1 for i in non_joker_counts]):
        return Hand.ONE_PAIR
    return Hand.HIGH_CARD

def get_hand_parser(using_jokers=False):
    if not using_jokers:
        return get_hand_type
    return get_hand_type_with_jokers

def compare_hands(hand1: str, hand2: str, using_jokers=False) -> HandComparison:
    hand_parser = get_hand_parser(using_jokers)
    hand1_type = hand_parser(hand1)
    hand2_type = hand_parser(hand2)

    if hand1_type.value > hand2_type.value:
        return HandComparison.HAND_1
    if hand2_type.value > hand1_type.value:
        return HandComparison.HAND_2
    
    for card1, card2 in zip(hand1, hand2):
        card1_type = get_card_type(card1, using_jokers)
        card2_type = get_card_type(card2, using_jokers)
        if card1_type.value > card2_type.value:
            return HandComparison.HAND_1
        if card2_type.value > card1_type.value:
            return HandComparison.HAND_2
    
    return HandComparison.TIE

def run_game(using_jokers = False):
    bid_lookup = dict() # {hand: bid}
    ranked_hands = [] # [hand] from lowest to highest rank
    lines = get_input()
    for line in lines:
        hand, bid = line.split()
        bid_lookup[hand] = int(bid)
        if not ranked_hands:
            ranked_hands.append(hand)
        else:
            for position, already_ranked_hand in enumerate(ranked_hands):
                res = compare_hands(hand, already_ranked_hand, using_jokers)
                if res == HandComparison.HAND_2:
                    ranked_hands.insert(position, hand)
                    break
            else:
                ranked_hands.append(hand)

    total_winnings = 0

    for position, entry in enumerate(ranked_hands):
        total_winnings += bid_lookup[entry] * (position + 1)

    print(total_winnings)

def part1():
    run_game(False)

def part2():
    run_game(True)

if __name__ == "__main__":
    part1()
    part2()