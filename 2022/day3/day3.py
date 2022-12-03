def get_input():
    with open('2022/day3/input.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines


priority = dict(zip('abcdefghijklmnopqrstuvwzyz', range(1,27)))
priority.update(dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', range(27,53))))


def part1():
    lines = get_input()

    s = 0

    for line in lines:
        l0, l1 = line[0:len(line)//2], line[len(line)//2:]
        inter = set(l0).intersection(set(l1))
        s += priority[inter.pop()]


    print(s)


def part2():
    lines = get_input()

    s = 0

    for i in range(2, len(lines), 3):
        l1 = lines[i-5]
        l2 = lines[i-4]
        l3 = lines[i-3]

        inter = set(l1).intersection(l2).intersection(l3)
        s += priority[inter.pop()]

    print(s)


if __name__ == "__main__":
    part1()
    part2()