
with open('./inputs/07_input.txt') as f:
    lines = f.read().splitlines()

lines = [[0 if char == '.' else 2 if char == '^' else 1 for char in line] for line in lines]
splitcount, LI = 0, lines[0]

for line in lines[1:]:
    constructed = [0] * len(line)
    for i in range(len(lines[0])):
        if LI[i] and not line[i]:
            constructed[i]= 1
        elif LI[i] and line[i]:
            constructed[i-1]=1
            constructed[i+1]=1
            splitcount+=1

    LI = constructed
    
print(splitcount)

for line in lines[::-1]:
    cs = [0] * len(line)
    for idx, char in enumerate(line):
        if not char:
            cs[idx]=LI[idx]
        else:
            cs[idx] = LI[idx-1] + LI[idx+1]

    LI=cs

start = lines[0].index(1)
print(LI[start])

