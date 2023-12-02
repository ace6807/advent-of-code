string_digits = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

def get_input() -> list[str]:
    with open('2023/day1/input.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines

def part1() -> int:
    lines = get_input()
    digits = []
    first , last = "", ""
    for line in lines:
        for c in line:
            if c.isdigit():
                if not first:
                    first = c
                else:
                    last = c
        last = first if not last else last
        print(first, last)
        digits.append(int(first+last))
        first, last = "", ""
    return sum(digits)


def find(line: str):
    res = {line.find(dig):dig for dig in string_digits.keys() if dig in line}
    res.update( {line.rfind(dig):dig for dig in string_digits.keys() if dig in line} )
    return res
    # keys = map(line.find, string_digits.keys())
    # return {key:string_digits[key] for key in keys if key != -1}

def part2():
    lines = get_input()
    digits = []
    first_pos , last_pos = None, None
    first, last = "", ""
    for line_no, line in enumerate(lines):
        for n, c in enumerate(line):
            if c.isdigit():
                if first_pos is None:
                    first_pos = n
                else:
                    last_pos = n
        if not last_pos:
            last_pos = first_pos

        
        string_dig_positions = find(line)
        min_string_dig_pos = min(string_dig_positions.keys()) if string_dig_positions else 100
        max_string_dig_pos = max(string_dig_positions.keys()) if string_dig_positions else -1

        if min_string_dig_pos < first_pos:
            first = string_digits[string_dig_positions[min_string_dig_pos]]
        else:
            first = line[first_pos]

        if max_string_dig_pos > last_pos:
            last = string_digits[string_dig_positions[max_string_dig_pos]]
        else:
            last = line[last_pos]            

        print(f"{line_no +1}: {first}{last}")

        digits.append(int(first+last))
        first, last = "", ""
        first_pos , last_pos = None, None       
    return sum(digits)
    

if __name__ == "__main__":
    # print(part1())
    print(part2())