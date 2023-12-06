import sys

def get_input():
    with open('2023/day5/input2.txt') as f:
        lines = [i for i in f.read().splitlines()]
    return lines


def get_mapping_for_source(almanac, section, source_number):
    mapping = next((mapping for mapping in almanac[section] if source_number >= mapping['source_range'][0] and source_number <= mapping['source_range'][1]), None)
    if mapping:
        return {'offset': source_number - mapping['source_range'][0], 'mapping': mapping}
    
    return {'offset': 0, 'mapping': {
        'source_range': (source_number, source_number),
        'dest_range': (source_number, source_number)
    }}


def get_dest_range_for_source(almanac, section, source_number):
    mapping = get_mapping_for_source(almanac, section, source_number)
    return {'offset': mapping["offset"], 'dest_range': mapping['mapping']['dest_range']}


def get_dest_for_source(almanac, section, source_number):
    dest_range = get_dest_range_for_source(almanac, section, source_number)
    return dest_range['dest_range'][0] + dest_range['offset']


def get_location_for_seed(almanac, seed_number):
    soil_number = get_dest_for_source(almanac, 'seed-to-soil', seed_number)
    fertilizer_number = get_dest_for_source(almanac, 'soil-to-fertilizer', soil_number)
    water_number = get_dest_for_source(almanac, 'fertilizer-to-water', fertilizer_number)
    light_number = get_dest_for_source(almanac, 'water-to-light', water_number)
    temperature_number = get_dest_for_source(almanac, 'light-to-temperature', light_number)
    humidity_number = get_dest_for_source(almanac, 'temperature-to-humidity', temperature_number)
    location_number = get_dest_for_source(almanac, 'humidity-to-location', humidity_number)
    return location_number


def part1():
    lines = get_input()
    seeds = [int(i) for i in lines[0].split(":")[1].strip().split(" ")]

    almanac = dict()
    current_section = None

    for line in lines[1:]:
        if not line:
            # throw away empty lines
            pass
        else:
            # handle section header
            if not line[0].isdigit():
                header = line.split(" ")[0]
                almanac[header] = []
                current_section = header
            else:
                dest_range_start, source_range_start, range_length = [int(i) for i in line.split(" ")]
                almanac[current_section].append({
                    'source_range': (source_range_start, source_range_start + range_length - 1),
                    'dest_range': (dest_range_start, dest_range_start + range_length - 1),
                })
    

    locations = [get_location_for_seed(almanac, seed) for seed in seeds]
    print(min(locations))


def part2():
    lines = get_input()
    seeds = iter(int(i) for i in lines[0].split(":")[1].strip().split(" "))

    almanac = dict()
    current_section = None

    for line in lines[1:]:
        if not line:
            # throw away empty lines
            pass
        else:
            # handle section header
            if not line[0].isdigit():
                header = line.split(" ")[0]
                almanac[header] = []
                current_section = header
            else:
                dest_range_start, source_range_start, range_length = [int(i) for i in line.split(" ")]
                almanac[current_section].append({
                    'source_range': (source_range_start, source_range_start + range_length - 1),
                    'dest_range': (dest_range_start, dest_range_start + range_length - 1),
                })


    # locations = [get_location_for_seed(almanac, seed) for seed in seeds]
    # print(min(locations))

    min_location = sys.maxsize

    for i in seeds:
        l = next(seeds)
        print(i, l)

        for seed_num in range(i, i+l):
            loc = get_location_for_seed(almanac, seed_num)
            if loc < min_location:
                min_location = loc
                print(min_location)

    print(min_location)

if __name__ == "__main__":
    # part1()
    part2()