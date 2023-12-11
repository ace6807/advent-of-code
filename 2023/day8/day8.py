from itertools import cycle
from math import lcm

def get_input() -> list[str]:
    with open('2023/day8/input.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines

def make_map(lines):
    map = dict()
    for line in lines:
        line = line.split("=")
        key = line[0].strip()
        l,r = line[1].strip().split(',')
        map[key] = {'L': l[1:], 'R': r[1:-1]}
    return map

def get_starting_locations(map: dict):
    return [key for key in map.keys() if key.endswith('A')]


def part1():
    lines = get_input()
    instructions = lines[0]
    map = make_map(lines[2:])

    location = 'AAA'
    steps = 0
    while True:
        for instruction in instructions:
            location = map[location][instruction]
            steps += 1
            if location == 'ZZZ':
                return steps

def part2():
    lines = get_input()
    instructions = lines[0]
    game_map = make_map(lines[2:])
    locs = get_starting_locations(game_map)
    steps = 0

    distances = []

    for pos in range(len(locs)):
        i = cycle(instructions)
        steps = 0
        while not locs[pos].endswith('Z'):
            instruction = next(i)
            locs[pos] = game_map[locs[pos]][instruction]
            steps += 1 
        distances.append(steps)

    return lcm(*distances)


if __name__ == "__main__":
    print(part1())
    print(part2())