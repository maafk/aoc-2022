import os 
this_file = os.path.realpath(__file__)
this_dir = os.path.dirname(this_file)
"""
A - rock
B - paper
C - scissors

X - rock
Y - paper
Z - scissors
"""
score_map = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "lose": 0,
    "draw": 3,
    "win": 6,
}
win_lose_map = {
    "AX": "draw",
    "AY": "win",
    "AZ": "lose",
    "BX": "lose",
    "BY": "draw",
    "BZ": "win",
    "CX": "win",
    "CY": "lose",
    "CZ": "draw",

}
def part_1(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()]
    score = 0
    for line in lines:
        split = line.split(" ")
        opp = split[0]
        you = split[1]
        
        # add based on what you chose
        score += score_map[you]
        # Did you win?
        score += score_map[win_lose_map["".join(split)]]
    return score
   

def part_2(input):
    with open(f"{this_dir}/{input}", "r") as f:
        lines = [x.strip() for x in f.readlines()]

    outcomes = {
        "X": "lose",
        "Y": "draw",
        "Z": "win"
    }
    score = 0
    for line in lines:
        split = line.split(" ")
        opp = split[0]
        outcome = split[1]
        # add score for outcome
        score += score_map[outcomes[outcome]]
        # figure out what we need to throw
        to_throw = {"x":x[1] for (x,y) in win_lose_map.items() if x.startswith(opp) and y == outcomes[outcome]}["x"]
        score += score_map[to_throw]
    return score

if __name__ == "__main__":
    part_1_result = part_1("input")
    part_2_result = part_2("input")
    print(f"part1: {part_1_result}")
    print(f"part2: {part_2_result}")