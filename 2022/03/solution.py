file = open("input.txt")
input_raw = file.read().splitlines()

#################################
# Part 1
#################################

def getScoreOfLetter(l):
    if ord(l) >= 97:
        return ord(l) - 96
    else:
        return ord(l) - 65 + 27

score = 0
    
for rucksack in input_raw:
    first = rucksack[:len(rucksack)//2]
    second = rucksack[len(rucksack)//2:]

    duplicates = [l for l in first if l in second]

    score += getScoreOfLetter(duplicates[0]) # only for this first douplicate

print("Solution Part 1:", score)

#################################
# Part 2
#################################

score = 0
for i in range(len(input_raw)//3):
    elveGroup = input_raw[i*3:i*3+3]

    duplicates = [l for l in elveGroup[0] if l in elveGroup[1] and l in elveGroup[2]]

    score += getScoreOfLetter(duplicates[0]) # only for this first douplicate

print("Solution Part 2:", score)