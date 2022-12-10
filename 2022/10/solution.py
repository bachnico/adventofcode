import numpy as np

file_handler = open("./input.txt")
input_raw = file_handler.read().splitlines()

def applyFunctionToInput(invokeFunction):
    registerValue = 1
    cycles = 0
    
    for instruction in input_raw:
        if instruction == "noop":
            invokeFunction(cycles, registerValue)
            cycles += 1
        else:
            [inst, value] = instruction.split(" ")
            invokeFunction(cycles, registerValue)
            cycles += 1
            invokeFunction(cycles, registerValue)
            cycles += 1
            registerValue += int(value)

#################################
# Part 1
#################################

def calcSignalStrength(cycle, register):
    global sumOfSignalStrength
    if cycle == 20 or (cycle > 20 and (cycle - 20) % 40 == 0):
        print(cycle, register * cycle)
        sumOfSignalStrength += register * cycle


            
sumOfSignalStrength = 0 
applyFunctionToInput(calcSignalStrength)
print("Solution Part 1:", sumOfSignalStrength)

#################################
# Part 2
#################################

def drawCRT(cycle, register):
    if cycle % 40 == 0:
        print()
        
    if abs(register - (cycle % 40)) <= 1:
        print("#", end = '')
    else:
        print(".", end = '')
    
applyFunctionToInput(drawCRT)

print("")
print("Solution Part 2:", "RFKZCPEF")