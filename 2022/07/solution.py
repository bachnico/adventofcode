import re

file = open("input.txt")
input_raw = file.read().splitlines()

def readFileSizes(startIndex, directoryName):
    pointer = startIndex
    size = 0
    
    sub_directories = []
    
    while pointer < len(input_raw):
        if "$ ls" in input_raw[pointer] or "dir " in input_raw[pointer]:
            pointer += 1
        elif "$ cd " in input_raw[pointer]:
            directory = re.findall(".* cd ([\w\/\.]+)", input_raw[pointer])[0]
            pointer += 1
        
            if directory == "..":
                sub_directories.insert(0, (directoryName, size))
                return pointer, sub_directories, size
            
            pointer, directories_new, new_size = readFileSizes(pointer, directoryName + directory + "/")
            
            sub_directories += directories_new
            size += new_size
        else:
            [fileSize, file] = input_raw[pointer].split(" ")
            size += int(fileSize)
            pointer += 1
    
    sub_directories.insert(0, (directoryName, size))    
    return pointer, sub_directories, size

pointer, directories, size = readFileSizes(1, "/")

#################################
# Part 1
#################################

output = 0
for (directory, size) in directories:
    if size <= 100000:
        output += size

print("Solution Part 1:", output)

#################################
# Part 2
#################################

totalUsed = int(directories[0][1])

totalCapacity = 70000000
hasToBeFree = 30000000

candidates = []
for (directory, size) in directories:
    if totalCapacity - totalUsed + size >= hasToBeFree:
        candidates.append(size)
        
candidates.sort()

print("Solution Part 2:", candidates[0])