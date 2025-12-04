#A little intoxicated (very).
#The first thought that comes to mind is that the search space for 2 digits is very small...
# If the second leg of the program is 1000 digits, it'd be a problem if I designed something that works for two digits.
# But I don't know what AOC wants yet.

with open('./inputs/03_input.txt') as f:
    series = f.readlines()

jolts = []
for line in series:
    line, cons = line[:-1], dict()
    jolts.append(sorted((d,len(line)-p-1) for p,d in enumerate(line))[::-1])

#Python supports string comparison by ord I believe(?) .. so 9>1, but 11<9. Single digits!
rs, NUM = 0, 12
for bank in jolts:
    construct = ''
    used = [float('inf')] 

    for i in range(NUM-1,-1,-1):
        for d,p in bank:
            if p>=i and used[-1] > p and p not in used:
                construct+=d
                used.append(p)
                break

    rs+=int(construct)

print(rs)
