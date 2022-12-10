# Read input and setup tasks
import numpy as np

file_handler = open("./input.txt")
input_raw = file_handler.read().splitlines()


def fixTail(head, tail):
    difference = head[0]-tail[0], head[1]-tail[1]
    
    if abs(difference[0]) + abs(difference[1]) > 2:
        # move both in x and y axis
        tail = (tail[0] + np.sign(difference[0]), tail[1])
        tail = (tail[0], tail[1] + np.sign(difference[1]))
    elif abs(difference[0]) > 1:
        # move in x axis
        tail = (tail[0] + np.sign(difference[0]), tail[1])
    elif abs(difference[1]) > 1:
        # move in y axis
        tail = (tail[0], tail[1] + np.sign(difference[1]))

    return tail

def simulateTail(knots):
    recentTailPlaces = []

    for line in input_raw:
        [direction, steps] = line.split(" ")
        steps = int(steps)

        for _ in range(steps):
            if direction == "R":
                knots[0] = (knots[0][0] + 1,  knots[0][1])
            elif direction == "L":
                knots[0] = (knots[0][0] - 1, knots[0][1])
            elif direction == "U":
                knots[0] = (knots[0][0], knots[0][1] - 1)
            elif direction == "D":
                knots[0] = (knots[0][0], knots[0][1] + 1)

            for i in range(1, len(knots)):
                knots[i] = fixTail(knots[i-1], knots[i])

            recentTailPlaces.append(knots[-1])
            
    return set(recentTailPlaces)

#################################
# Part 1
#################################

knots = [(0,0)] * 2
print("Solution Part 1:", len(simulateTail(knots)))

#################################
# Part 2
#################################

knots = [(0,0)] * 10
print("Solution Part 2:", len(simulateTail(knots)))