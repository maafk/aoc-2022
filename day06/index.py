from collections import deque
import os 
this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)

def act_on_line(line, non_repeating: int):
    d = deque(maxlen=non_repeating)
    for i, ch in enumerate(line):
        d.append(ch)
        d_as_list = list(d)
        if len(d_as_list) < non_repeating:
            continue
        if len(d_as_list) > non_repeating:
            d.popleft()
        duplicates = [x for x in d_as_list if d_as_list.count(x) > 1]
        if not duplicates:
            return i + 1
def part_1(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
    for line in lines:
        return act_on_line(line, 4)
   

def part_2(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
    for line in lines:
        return act_on_line(line, 14)

if __name__ == "__main__":
    part_1_result = part_1("input")
    part_2_result = part_2("input")
    print(f"part1: {part_1_result}")
    print(f"part2: {part_2_result}")