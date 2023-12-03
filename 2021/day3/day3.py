def get_input():
    with open('2021/day3/input.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines


def part1():
    gama_bits = [[0] for _ in range(12)]
    epsilon_bits = [[0] for _ in range(12)]

    bits = [[0] for _ in range(12)]
    for line in get_input():
        for pos, bit in enumerate(line):
            bits[pos][0] += int(bit)

    for pos, bit in enumerate(bits):
        if bit[0] > 500:
            gama_bits[pos] = 1
            epsilon_bits[pos] = 0
        else:
            gama_bits[pos] = 0
            epsilon_bits[pos] = 1
    
    gama_rate =    int("0b"+"".join([str(bit) for bit in gama_bits]), 2)
    epsilon_rate = int("0b"+"".join([str(bit) for bit in epsilon_bits]), 2)
    
    return gama_rate * epsilon_rate
        

def part2():
    ...


if __name__ == "__main__":
    print(part1())
    part2()