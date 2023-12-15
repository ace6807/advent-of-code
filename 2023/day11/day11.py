from itertools import combinations


def get_input():
    with open('2023/day11/input.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines

def print_atlas(atlas):
    for row in atlas:
        print(row)
    print("="*len(atlas[0]))

def get_location_data(x, y, atlas):
    return atlas[y][x]

def map_space(image) -> list[list[str]]:
    atlas = []
    for line in image:
        atlas.append([c for c in line])
    return atlas

def expand_atlas(atlas: list[list[str]]):
    for row in range(len(atlas)-1, -1, -1):
        if '#' not in atlas[row]:
            atlas.insert(row, atlas[row].copy())
    
    empty_cols = []
    for col in range(len(atlas[0])-1, -1, -1):
        # print(f"col: {col}")
        if '#' not in [atlas[row][col] for row in range(len(atlas))]:
            empty_cols.append(col)

    for row in range(len(atlas)):
        for empty_col in empty_cols:
            atlas[row].insert(empty_col, '.')

    return atlas

def get_galaxy_map(atlas: list[list[str]]) -> dict[int, tuple]:
    galaxies = dict()
    galaxy_count = 0
    for y in range(len(atlas)):
        for x in range(len(atlas[0])):
            if get_location_data(x,y, atlas) == '#':
                galaxies[galaxy_count] = (x,y)
                galaxy_count += 1
    return galaxies

def calculate_galaxy_distances(galaxy_map: dict[int, tuple]) -> int:
    distances = []
    for pair in combinations(galaxy_map.keys(), 2):
        p1 = galaxy_map[pair[0]]
        p2 = galaxy_map[pair[1]]
        distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        distances.append(distance)
    return sum(distances)

def part1():
    atlas = map_space(get_input())
    atlas = expand_atlas(atlas)
    galaxy_map = get_galaxy_map(atlas)
    total_distance = calculate_galaxy_distances(galaxy_map)
    print(total_distance)

def part2():
    ...


if __name__ == "__main__":
    part1()
    part2()