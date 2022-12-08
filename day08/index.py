
import os 
this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)

def multiply_list(list) :
    result = 1
    for i in list:
         result = result * i
    return result

def part_1(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
    visible = 0
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            # get list of trees on each side, going to the edge
            trees_above = [int(lines[t][x]) for t in range(y)]
            trees_below = [int(lines[t][x]) for t in range(y + 1,len(lines))]
            trees_left = [int(lines[y][t]) for t in range(x)]
            trees_right = [int(lines[y][t]) for t in range(x + 1,len(lines[0]))]

            # if any empty, it's at the edge
            if not all([trees_above, trees_below, trees_left, trees_right]):
                visible += 1
                continue
            # combine all trees
            all_trees = [trees_above, trees_below, trees_left, trees_right]
            if any((max(trees) < int(ch) for trees in all_trees)):
                visible += 1
            
    return visible

def part_2(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
    max_score = 0
    for y, line in enumerate(lines):
        for x, ch in enumerate(line):
            # get list of trees on each side, going to the edge
            trees_above = [int(lines[t][x]) for t in range(y)]
            trees_below = [int(lines[t][x]) for t in range(y + 1,len(lines))]
            trees_left = [int(lines[y][t]) for t in range(x)]
            trees_right = [int(lines[y][t]) for t in range(x + 1,len(lines[0]))]

            if not all([trees_above, trees_below, trees_left, trees_right]):
                continue
            trees_above_viewable = 0
            trees_below_viewable = 0
            trees_left_viewable = 0
            trees_right_viewable = 0

            # get above and left in right order
            trees_above.reverse()
            trees_left.reverse()
            
            for tree in trees_above:
                trees_above_viewable += 1
                if tree >= int(ch):
                    break
                
            for tree in trees_below:
                trees_below_viewable += 1
                if tree >= int(ch):
                    break
            for tree in trees_left:
                trees_left_viewable += 1
                if tree >= int(ch):
                    break
                
            for tree in trees_right:
                trees_right_viewable += 1
                if tree >= int(ch):
                    break
            trees_viewable = [trees_above_viewable, trees_below_viewable, trees_left_viewable, trees_right_viewable]

            scene_score = multiply_list(trees_viewable)

            max_score = scene_score if scene_score > max_score else max_score
    return max_score

if __name__ == "__main__":
    part_1_result = part_1("sample_input")
    part_2_result = part_2("input")
    print(f"part1: {part_1_result}")
    print(f"part2: {part_2_result}")