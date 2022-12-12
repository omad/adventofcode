import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()


shape_score = dict(A=1, B=2, C=3)

# A Rock
# B Paper
# C Scissors


def round_score(opponent, mine):
    mine = chr(ord(mine) - 23)
    if opponent == mine:
        return 3 + shape_score[mine]
    if mine == "A" and opponent == "C" or mine == "B" and opponent == "A" or mine == "C" and opponent == "B":
        return 6 + shape_score[mine]
    else:
        return shape_score[mine]

# X = lose
# Y = draw
# Z = win
def round_score_2(o, m):
    if m == "Y":
        return 3 + shape_score[o]
    if m == "X":
        # Lose
        # Them to me
        mine = {"A": "C", "B": "A", "C": "B"}[o]
        return 0 + shape_score[mine]
    if m == "Z":
        # win
        mine = {"A": "B", "B": "C", "C": "A"}[o]
        return 6 + shape_score[mine]
    

score = 0
score_2 = 0
for line in lines:
    o, m = line[0], line[2]
    score += round_score(o, m)
    score_2 += round_score_2(o, m)

print(score)
print(score_2)


    
