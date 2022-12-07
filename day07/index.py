import os
this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)

from collections import defaultdict

def create_fs_map(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
    structure = defaultdict(int)
    dir_stack = []
    for line in lines:
        if line == "$ ls":
            continue
        if line.startswith("dir"):
            continue
        if line.startswith("$ cd"):
            line_split = line.split()
            dir_dest = line_split[-1]
            if dir_dest == "..":
                dir_stack.pop()
            else:
                dir_stack.append(dir_dest)
            continue

        # must be a file now
        split = line.split()
        file_size = int(split[0])
        ## Add file size to all parent directories
        for i in range(len(dir_stack) + 1):
            structure[".".join(dir_stack[:i])] += file_size
    return structure

def part_1(input):
    structure = create_fs_map(input)
    answer = 0
    for p in structure:
        if structure[p] <= 100000:
            answer += structure[p]
    return answer


def part_2(input):
    structure = create_fs_map(input)
    total_available = 70000000
    space_needed = 30000000
    total_used = structure["/"]
    space_to_free_up = space_needed - (total_available - total_used)
    # sort smallest to largest
    sorted_structure = sorted(structure.values())
    # see if bigger than space needed to free up
    for s in sorted_structure:
        if s >= space_to_free_up:
            return s

if __name__ == "__main__":
    part_1_result = part_1("input")
    part_2_result = part_2("input")
    print(f"part1: {part_1_result}")
    print(f"part2: {part_2_result}")