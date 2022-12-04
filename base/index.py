import os 
this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)

def part_1(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
    
   

def part_2(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
    

if __name__ == "__main__":
    part_1_result = part_1("input")
    part_2_result = part_2("input")
    print(f"part1: {part_1_result}")
    print(f"part2: {part_2_result}")