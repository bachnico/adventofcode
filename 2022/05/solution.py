import re

file_handler = open("./input.txt")
input_raw = file_handler.read().splitlines()

crates_in, moves = input_raw[:8], input_raw[10:]

def initializeCrates():
    crates = [[], [], [], [], [], [], [], [], []]
    
    for crateLine in crates_in:
        items = crateLine[1::4]
    
        for i, item in enumerate(items):
            if item != " ":
                crates[i].insert(0, item)

    return crates

def printCrates(crates):
    for crate in crates:
        print(crate[-1], end="")

#################################
# Part 1
#################################

crates = initializeCrates()

for move in moves:
    [mv, fr, to] = [int(x) for x in re.findall("move (\d+) from (\d+) to (\d+)", move)[0]]
    [fr, to] = [fr - 1, to -1]
    
    for i in range(mv):
        crates[to].append(crates[fr][-1])
        crates[fr] = crates[fr][:-1]

print("Solution Part 1:")
printCrates(crates)

#################################
# Part 2
#################################

crates = initializeCrates()

for move in moves:
    [mv, fr, to] = [int(x) for x in re.findall("move (\d+) from (\d+) to (\d+)", move)[0]]
    [fr, to] = [fr - 1, to -1]
    
    top = crates[fr][-mv:]
    crates[to].extend(top)
    crates[fr] = crates[fr][:-mv]

print("Solution Part 2:")
printCrates(crates)