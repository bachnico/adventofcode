file = open("input.txt")
input = file.read().splitlines()

#################################
# Part 1
#################################

caloriesByElves = []

current = 0
for calorie in input:
    if calorie == "":
        caloriesByElves.append(int(current))
        current = 0
    else:
        current += int(calorie)

caloriesByElves.sort()

print("Solution Part 1:", caloriesByElves[-1])

#################################
# Part 2
#################################

print("Solution Part 2:", caloriesByElves[-1] + caloriesByElves[-2] + caloriesByElves[-3])
