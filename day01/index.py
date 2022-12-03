import os 
this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)
def part_1(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()] + [""]
    
    elf_calorie_count = []
    current_count = 0
    for line in lines:
        if not line:
            elf_calorie_count.append(current_count)
            current_count = 0
        else:
            current_count += int(line)

    return max(elf_calorie_count)

def part_2(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()] + [""]
    
    elf_calorie_count = []
    current_count = 0
    for line in lines:
        if not line:
            elf_calorie_count.append(current_count)
            current_count = 0
        else:
            current_count += int(line)

    elf_calorie_count.sort(reverse=True)
    return sum(elf_calorie_count[:3])

if __name__ == "__main__":
    part_1_result = part_1("input")
    part_2_result = part_2("input")
    print(f"part1: {part_1_result}")
    print(f"part2: {part_2_result}")