ROCK = 1
PAPER = 2
SCISSORS = 3

LOSE = 0
TIE = 3
WIN = 6

hands = {
    ("A", "X"): TIE + ROCK,
    ("A", "Y"): WIN + PAPER,
    ("A", "Z"): LOSE + SCISSORS,

    ("B", "X"): LOSE + ROCK,
    ("B", "Y"): TIE + PAPER,
    ("B", "Z"): WIN + SCISSORS,

    ("C", "X"): WIN + ROCK,
    ("C", "Y"): LOSE + PAPER,
    ("C", "Z"): TIE + SCISSORS,
}

lines =  [line.strip() for line in open("2022/day2/input.txt")]
sum = 0
for line in lines:
    hand = tuple(line.split())
    sum += hands[hand]

print(sum)


hands = {
    ("A", "X"): LOSE + SCISSORS,
    ("A", "Y"): TIE + ROCK,
    ("A", "Z"): WIN + PAPER,

    ("B", "X"): LOSE + ROCK,
    ("B", "Y"): TIE + PAPER,
    ("B", "Z"): WIN + SCISSORS,

    ("C", "X"): LOSE + PAPER,
    ("C", "Y"): TIE + SCISSORS,
    ("C", "Z"): WIN + ROCK,

}

lines =  [line.strip() for line in open("2022/day2/input.txt")]
sum = 0
for line in lines:
    hand = tuple(line.split())
    sum += hands[hand]

print(sum)
