def get_input():
    with open('2021/day1/input.txt') as f:
        lines = [int(i) for i in f.read().splitlines()]
    return lines


def part1():
    lines = get_input()
    prev = lines[0]
    increase = 0
    for line in lines[1:]:
        if line > prev:
            increase += 1
        prev = line

    print(increase)



def part2():
    lines = get_input()
    increases = 0
    for i in range(3, len(lines)):
        if sum(lines[i-2:i+1]) > sum(lines[i-3:i]):
            increases += 1

    print(increases)
        


if __name__ == "__main__":
    part1()
    part2()