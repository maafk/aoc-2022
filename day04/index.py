import os 
this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)

def part_1(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
    fully_contained = 0
    for line in lines:
        # split left right
        left, right = line.split(",")
        left_min, left_max = [int(x) for x in left.split("-")]
        right_min, right_max = [int(x) for x in right.split("-")]

        # check if left in right
        if left_min >= right_min and left_max <= right_max:
            fully_contained += 1
            continue
        # check if right in left
        if right_min >= left_min and right_max <= left_max:
            fully_contained += 1
            continue

    return fully_contained
   

def part_2(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
    partially_contained = 0
    for line in lines:
        # split left right
        left, right = line.split(",")
        left_min, left_max = [int(x) for x in left.split("-")]
        right_min, right_max = [int(x) for x in right.split("-")]

        # find where no overlap
        if (left_max < right_min) or (left_min > right_max):
            pass
        else:
            # some kind of overlap
            partially_contained += 1

    return partially_contained
    

if __name__ == "__main__":
    part_1_result = part_1("input")
    part_2_result = part_2("input")
    print(f"part1: {part_1_result}")
    print(f"part2: {part_2_result}")