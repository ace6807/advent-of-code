def get_input():
    with open('2023/day9/input.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines

def build_history(current_history):
    if all(i == 0 for i in current_history):
        return current_history
    else:
        new_line = [current_history[pos] - current_history[pos-1] for pos in range(1, len(current_history[1:]) + 1)]
        new_line = build_history(new_line)
        return current_history + [current_history[-1] + new_line[-1]]

def build_history_left(current_history):
    if all(i == 0 for i in current_history):
        return current_history
    else:
        new_line = [current_history[pos] - current_history[pos-1] for pos in range(1, len(current_history[1:]) + 1)]
        new_line = build_history_left(new_line)
        return [current_history[0] - new_line[0]] + current_history

def part1():
    lines = get_input()

    history = dict()
    for pos,line in enumerate(lines):
        current_history = [int(i) for i in line.split(" ")]
        new_history = build_history(current_history)
        history[pos] = new_history

    
    return sum([history[i][-1] for i in history])

def part2():
    lines = get_input()

    history = dict()
    for pos,line in enumerate(lines):
        current_history = [int(i) for i in line.split(" ")]
        new_history = build_history_left(current_history)
        history[pos] = new_history

    return sum([history[i][0] for i in history])

if __name__ == "__main__":
    print(part1())
    print(part2())