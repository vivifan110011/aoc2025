base,ap = 50,0
with open('./inputs/01_input.txt') as f:
    series = f.read().splitlines()

for term in series:
    if not base: penalty=0
    else: penalty=1

    if term[0]=='L':
        base-=int(term[1:])
    else:
        base+=int(term[1:])

    #bounds
    if base>0:
        ap+=abs(base//100)    
    else:
        ap+=abs(int(base/100))+penalty

    base%=100

print(ap)

