from functools import reduce

def get_input():
    with open('2023/day6/input2.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines

def get_num_ways_to_win(game):
    ways_to_win = 0
    for t in range(0, game[0]):
        if t * (game[0] - t) > game[1]:
            ways_to_win += 1 
    return ways_to_win

def part1():
    times, distances = [i.split(":")[1].strip().split() for i in get_input()]
    times = [int(i) for i in times]
    distances = [int(i) for i in distances]
    games = list(zip(times, distances))
    ways_to_win = [get_num_ways_to_win(game) for game in games]
    res = reduce(lambda x,y: x*y, ways_to_win)
    print(res)

def part2():
    times, distances = [i.split(":")[1].strip().split() for i in get_input()]
    times = [int("".join(times))]
    distances = [int("".join(distances))]    
    games = list(zip(times, distances))

    games = [(47707566, 282107911471062)]

    ways_to_win = [get_num_ways_to_win(game) for game in games]
    res = reduce(lambda x,y: x*y, ways_to_win)
    print(res)


if __name__ == "__main__":
    part1()
    part2()