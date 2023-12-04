from dataclasses import dataclass

@dataclass
class Point:
    def __hash__(self) -> int:
        return hash((self.x, self.y))

    x: int
    y: int

def get_input():
    with open('2023/day3/input.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines

def get_adjacents(point: Point, maxes: Point):
    x_min = max(0, point.x - 1)
    y_min = max(0, point.y - 1)
    x_max = min(maxes.x, point.x + 1)
    y_max = min(maxes.y, point.y + 1)
    return set(Point(x,y) for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1))



def part1():
    lines = get_input()

    symbols = dict()
    for line_no, line in enumerate(lines):
        for col_num, c in enumerate(line):
            if c != '.' and not c.isdigit():
                symbols[Point(line_no, col_num)] = c

    part_num_stack = []
    for line_no, line in enumerate(lines):
        num_stack = []
        symbol_detected = False
        for col_num, c in enumerate(line):
            if c.isdigit():
                num_stack.append(c)
                adjacent_positions = get_adjacents(Point(line_no, col_num), Point(len(lines[0]) - 1, len(lines) - 1))
                if not symbol_detected:
                    symbol_detected = any([(pos in symbols) for pos in adjacent_positions])
            else:
                if num_stack and symbol_detected:
                    part_num_stack.append(int("".join(num_stack)))
                
                num_stack.clear()
                symbol_detected = False
        if num_stack:
            # If we ran over the end of the line, see if the part number is valid and clean up
            if symbol_detected:
                part_num_stack.append(int("".join(num_stack)))
                num_stack.clear()
  
    print(sum(part_num_stack))


def part2():
    lines = get_input()

    symbols = dict()
    for line_no, line in enumerate(lines):
        for col_num, c in enumerate(line):
            if c == '*' and not c.isdigit():
                symbols[Point(line_no, col_num)] = []

    part_num_stack = []
    for line_no, line in enumerate(lines):
        num_stack = []
        found_symbols = set()
        for col_num, c in enumerate(line):
            if c.isdigit():
                num_stack.append(c)
                adjacent_positions = get_adjacents(Point(line_no, col_num), Point(len(lines[0]) - 1, len(lines) - 1))
                found_symbols.update(set(pos for pos in adjacent_positions if (pos in symbols)))
            else:
                if num_stack and found_symbols:
                    part_num = int("".join(num_stack))
                    part_num_stack.append(part_num)
                    for symbol in found_symbols:
                        symbols[symbol].append(part_num)
                
                num_stack.clear()
                found_symbols = set()
        if num_stack:
            # If we ran over the end of the line, see if the part number is valid and clean up
            if found_symbols:            
                part_num = int("".join(num_stack))
                part_num_stack.append(part_num)
                for symbol in found_symbols:
                    symbols[symbol].append(part_num)

                num_stack.clear()

    total = sum([ symbols[symbol][0] * symbols[symbol][1] for symbol in symbols if len(symbols[symbol]) == 2 ])
    print(total)

if __name__ == "__main__":
    part1()
    part2()