import math

def euclidean_dist(a,b):
    return sum((i-j)**2 for i,j in zip(a,b))**.5

with open('inputs/08_input.txt') as f:
    lines = f.read().splitlines()
    jun = [tuple(map(int,l.split(','))) for l in lines]

euclideans = list()

for a in range(len(jun)-1):
    for b in range(a+1,len(jun)):
        euclideans.append((euclidean_dist(jun[a],jun[b]),a,b))

euclideans.sort()

circuits = [{euclideans[0][1],euclideans[0][2]}]
#LIM =  1000
for l, dist in enumerate(euclideans[1:]):
    a_check, b_check = -1, -1
    for i, c in enumerate(circuits):
        if a_check >= 0 and dist[2] in c:
            circuits[a_check] |= c
            del circuits[i]
            break
        elif b_check >=0 and dist[1] in c:
            circuits[b_check] |= c
            del circuits[i]
        else:
            jf = False
            if dist[1] in c:
                a_check = i
                jf=True
            if dist[2] in c:
                b_check = i
                jf=True
            if jf:
                circuits[i].update([dist[1],dist[2]])
                if a_check >=0 and b_check >= 0:
                    break

        
    if a_check<0 and b_check < 0: 
        circuits.append({dist[1],dist[2]})
    
    #if l == LIM-2:
        #break
    if len(jun) == len(circuits[0]):
        #p2 answer
        print(jun[dist[1]][0]*jun[dist[2]][0])
        break


lens = [len(c) for c in circuits]
lens.sort()
#p1 answer
print(math.prod(lens[-3:]))

    
