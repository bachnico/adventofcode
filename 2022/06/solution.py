file_handler = open("./input.txt")
input_raw = file_handler.read().splitlines()[0]

#################################
# Part 1
#################################

for i in range(len(input_raw)):
    substring = set(input_raw[i:i+4])
    if len(substring) == 4:
        print("Solution Part 1:")
        print(i + 4)
        break

#################################
# Part 2
#################################

for i in range(len(input_raw)):
    substring = set(input_raw[i:i+14])
    if len(substring) == 14:
        print("Solution Part 2:")
        print(i + 14)
        break