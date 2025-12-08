from functools import reduce
import operator

cleaned=[]
with open('inputs/06_input.txt') as f:
    for line in f.read().strip().split('\n'):
        cleaned.append([x for x in line.split(' ') if x])

rs=0
for i in range(len(cleaned[0])):
    if cleaned[len(cleaned)-1][i] == '*':
        op=operator.mul
    else:
        op=operator.add
    rs+=reduce(op,[int(cleaned[j][i]) for j in range(len(cleaned)-1)])

print(rs)


with open('inputs/06_input.txt') as f:
    ptr = [list(r) for r in f.read().splitlines()]

strplog, rs = [], 0
for i in range(1,len(ptr[0])+1):
    strip=[ptr[p][-i] for p in range(len(ptr))]
    
    if strip[-1]=='*': op=operator.mul
    elif strip[-1]=='+': op=operator.add

    if strip == [" "] * len(ptr):
        rs+=reduce(op,strplog)
        strplog=[]
    else:
        strplog.append(int("".join(strip[:-1]).replace(" ","")))

rs+=reduce(op,strplog)
print(rs)
