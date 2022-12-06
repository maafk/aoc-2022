import os 
this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)

def get_data(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = f.readlines()
    
    # find blank line
    blank_line = lines.index("\n")
    keys = lines[blank_line - 1].split()
    data_structure = {x: [] for x in keys}
    keys_count = len(keys)
    for i in range(blank_line - 2, -1, -1):
        line = lines[i].strip("\n")
        for j in range(1, keys_count + 1):

            
            crate = line[j * 4 - 3]
            if crate.strip():
                data_structure[keys[j -1]].append(crate)
    return data_structure

def get_steps(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = f.readlines()
    
    # find blank line
    blank_line = lines.index("\n")
    return [x.strip() for x in lines[blank_line + 1:]]

def part_1(input):
    
    struct = get_data(input)
    steps = get_steps(input)
    for step in steps:
        instructions = step.split()
        from_stack = instructions[3]
        to_stack = instructions[5]
        count = int(instructions[1])
        for i in range(count):
            popped = struct[from_stack].pop()
            struct[to_stack].append(popped)

    return "".join([struct[x][-1] for x in struct])
   

def part_2(input):
    struct = get_data(input)
    steps = get_steps(input)
    for step in steps:
        instructions = step.split()
        from_stack = instructions[3]
        to_stack = instructions[5]
        count = int(instructions[1])
        struct[to_stack] = struct[to_stack] + struct[from_stack][-count:]
        for i in range(count):
            struct[from_stack].pop()
            
    return "".join([struct[x][-1] for x in struct])
    

if __name__ == "__main__":
    part_1_result = part_1("input")
    part_2_result = part_2("input")
    print(f"part1: {part_1_result}")
    print(f"part2: {part_2_result}")