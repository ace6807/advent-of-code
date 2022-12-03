def get_input():
    with open('2021/day2/input.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines


def part1():
    lines = get_input()
    horizontal_pos = 0
    depth = 0

    for line in lines:
        direction, distance = line.split()
        if direction == 'down':
            depth += int(distance)
        elif direction == 'up':
            depth -= int(distance)
        elif direction == 'forward':
            horizontal_pos += int(distance)

    print(horizontal_pos * depth) 
    
def part2():
    lines = get_input()
    horizontal_pos = 0
    depth = 0
    aim = 0

    for line in lines:
        direction, distance = line.split()
        if direction == 'down':
            aim += int(distance)
        elif direction == 'up':
            aim -= int(distance)
        elif direction == 'forward':
            horizontal_pos += int(distance)
            depth += aim * int(distance)

    print(horizontal_pos * depth) 


if __name__ == "__main__":
    part1()
    part2()