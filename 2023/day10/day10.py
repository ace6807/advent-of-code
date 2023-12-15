from enum import Enum, auto


def get_input() -> list[str]:
    with open('2023/day10/input.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines


class Direction(Enum):
    RIGHT =  auto()
    DOWN  =  auto()
    LEFT  =  auto()
    UP    =  auto()

bounded_cache = dict()
can_reach_edge_cache = dict()


def parse_game_map(lines):
    start_location = tuple()
    game_map = dict()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            game_map[col,row] = char
            if char == 'S':
                start_location = (col,row)

    return game_map, start_location, (len(lines[0])-1, len(lines)-1)

def get_adjacent_locations(pos, board_width, board_height):
    row_min = max(0, pos[1] - 1)
    row_max = min(board_height, pos[1] + 1)
    col_min = max(0, pos[0] - 1)
    col_max = min(board_width, pos[0] + 1)

    locs = (
        (pos[0], row_min), # up
        (col_max, pos[1]), # right
        (pos[0], row_max), # down
        (col_min, pos[1]), # left
    )
    return tuple(loc for loc in locs if loc != pos and (loc[0] == pos[0] or loc[1] == pos[1]))

    # return set(
    #     (x,y) for y in range(row_min, row_max + 1) for x in range(col_min, col_max + 1) 
    #     if (x,y) != pos and (x == pos[0] or y == pos[1])
    # )

def get_edges(pos, bounds):
    edges = (
        (pos[0], 0),            # up
        (bounds[0], pos[1]),    # right
        (pos[0], bounds[1]),    # down
        (0, pos[1]),            # left
    )

    return edges

def parse_direction(location, destination):
    if destination[0] > location[0]:
        return Direction.RIGHT
    if destination[0] < location[0]:
        return Direction.LEFT
    if destination[1] > location[1]: 
        return Direction.DOWN
    if destination[1] < location[1]:
        return Direction.UP

def is_valid_path(location, destination, game_map):
    direction = parse_direction(location, destination)

    match direction:
        case Direction.RIGHT:
            if game_map[location] in ['S', '-', 'L', 'F'] and game_map[destination] in ['S', '-', 'J', '7']:
                return True
            return False
        case Direction.LEFT:
            if game_map[location] in ['S', '-', '7', 'J'] and game_map[destination] in ['S', '-', 'F', 'L']:
                return True
            return False
        case Direction.DOWN:
            if game_map[location] in ['S', '|', 'F', '7'] and game_map[destination] in ['S', '|', 'J', 'L']:
                return True
            return False
        case Direction.UP:
            if game_map[location] in ['S', '|', 'L', 'J'] and game_map[destination] in ['S', '|', 'F', '7']:
                return True
            return False

def get_valid_moves(location, bounds, game_map):
    adjacent_locations = get_adjacent_locations(location, bounds[0], bounds[1])
    valid_moves = [
        adjacent_location for adjacent_location in adjacent_locations 
        if is_valid_path(location, adjacent_location, game_map) and adjacent_location
    ]
    return valid_moves

def is_edge(pos, bounds):
    if pos[0] == 0 or pos[1] == 0 or pos[0] == bounds[0] or pos[1] == bounds[1]:
        return True
    return False

def walk_loop(game_map, start_location, bounds):
    last_move = start_location
    current_location = start_location
    steps = 0

    loop_map = dict()

    while steps == 0 or current_location != start_location:
        loop_map[current_location] = game_map[current_location]
        valid_moves = get_valid_moves(current_location, bounds, game_map)
        next_move = next(move for move in valid_moves if move != last_move)
        last_move = current_location
        current_location = next_move
        steps += 1
    
    return steps, loop_map

def is_enclosed(pos, game_map, loop_map, bounds):
    corner_stack = []
    boundry_counter = 0
    for x in range(0, pos[0]):
        if (x, pos[1]) in loop_map and game_map[x, pos[1]] in ['|', 'S']:
            boundry_counter +=1
        elif (x, pos[1]) in loop_map and game_map[x, pos[1]] in ['J', 'F', '7', 'L']:
            if not corner_stack:
                corner_stack.append((x, pos[1]))
            else:
                corner_tile = game_map[x, pos[1]]
                last_corner_tile = game_map[corner_stack.pop()]
                if last_corner_tile == 'L' and corner_tile == '7' or last_corner_tile == 'F' and corner_tile == 'J':
                    boundry_counter += 1  
    return not boundry_counter % 2 == 0


def part1():
    lines = get_input()
    game_map, start_location, bounds = parse_game_map(lines)
    steps, _ = walk_loop(game_map, start_location, bounds)
    print(steps//2)

def part2():
    lines = get_input()
    game_map, start_location, bounds = parse_game_map(lines)
    _, loop_map = walk_loop(game_map, start_location, bounds)

    bounded = 0
    for row, line in enumerate(lines):
        for col, c in enumerate(line):
            position = (col, row)
            if position not in loop_map and not is_edge(position, bounds):
                if is_enclosed(position, game_map, loop_map, bounds):
                    bounded += 1
    print(bounded)

if __name__ == "__main__":
    part1()
    part2()