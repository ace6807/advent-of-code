def get_input():
    with open("./2022/day4/input.txt") as f:
        lines = f.read().splitlines()
    return lines

def part1():
    lines = get_input()
    overlaps = 0
    for pair in lines:
        a,b = pair.split(',')
        a_start, a_end = (int(i) for i in a.split('-'))
        b_start, b_end = (int(i) for i in b.split('-'))
        a_set = set(range(a_start, a_end + 1))
        b_set = set(range(b_start, b_end + 1))

        if a_set.issubset(b_set) or b_set.issubset(a_set):
            overlaps += 1

    print(overlaps)


def part2():
    lines = get_input()
    overlaps = 0
    for pair in lines:
        a,b = pair.split(',')
        a_start, a_end = (int(i) for i in a.split('-'))
        b_start, b_end = (int(i) for i in b.split('-'))
        a_set = set(range(a_start, a_end + 1))
        b_set = set(range(b_start, b_end + 1))

        if a_set.intersection(b_set):
            overlaps += 1

    print(overlaps)




if __name__ == "__main__":
    # part1()
    part2()