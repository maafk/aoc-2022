import os 
this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)

scores = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part_1(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
    
    priority = 0
    for line in lines:
        half = int(len(line) / 2)
        first = line[:half]
        second = line[half:]
        common = [x for x in first if x in second][0]
        priority += scores.index(common)
    return priority
        

def part_2(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
    
    group_count = 0
    priority = 0
    group = []
    for line in lines:
        group.append(line)
        group_count += 1
        if len(group) == 3:
            common = [x for x in group[0] if x in group[1] and x in group[2]][0]
            priority += scores.index(common)
            group_count = 0
            group = []

    return priority

if __name__ == "__main__":
    part_1_result = part_1("input")
    part_2_result = part_2("input")
    print(f"part1: {part_1_result}")
    print(f"part2: {part_2_result}")