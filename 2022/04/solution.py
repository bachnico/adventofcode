file = open("input.txt")
input_raw = file.read().splitlines()

#################################
# Part 1
#################################

count = 0

for pair in input_raw:
    [[l1, u1], [l2, u2]] = [s.split("-") for s in pair.split(",")]
    
    l1 = int(l1)
    l2 = int(l2)
    u1 = int(u1)
    u2 = int(u2)
    
    if l2 > u2:
        print(pair, l1, u1, l2, u2, int(l2) > int(u2), l2 > u2, "dafuq?")
    
    if (l1 <= l2 and u2 <= u1) or (l2 <= l1 and u1 <= u2):
        count += 1

print("Solution Part 1:", count)
    
#################################
# Part 2
#################################

count = 0
for pair in input_raw:
    [[l1, u1], [l2, u2]] = [s.split("-") for s in pair.split(",")]
    
    l1 = int(l1)
    l2 = int(l2)
    u1 = int(u1)
    u2 = int(u2)
    
    if (l1 <= l2 and u1 >= l2) or (l2 <= l1 and u2 >= l1):
        count += 1
    
print("Solution Part 2:", count)