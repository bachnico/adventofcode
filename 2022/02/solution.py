file = open("input.txt")
input_raw = file.read().splitlines()

input = [lines.split(" ") for lines in input_raw]

#################################
# Part 1
#################################

XYZ = ["X", "Y", "Z"]
ABC = ["A", "B", "C"]

score = 0
for [opponent, me] in input:
    score += XYZ.index(me) + 1

    if(ABC.index(opponent) == XYZ.index(me)):
        score += 3

    if (ABC.index(opponent) - XYZ.index(me)) % 3 == 2:
        score += 6


print("Solution Part 1:", score) 

#################################
# Part 2
#################################

score = 0
for [opponent, outcome] in input:
    # X => lose => -1 in list
    # Y => draw => +0 in list
    # Z => win  => +1 in list
    # outcome   => index of XYZ - 1 

    me_index = (ABC.index(opponent) + XYZ.index(outcome) - 1) % 3

    score += me_index + 1           # Points for Rock, Paper, Sissors
    score += XYZ.index(outcome) * 3 # Points for Win, Draw, Lose
    
print("Solution Part 2:", score)