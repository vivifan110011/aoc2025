import math

with open('./inputs/02_input.txt') as f:
    ranges=[(int(a),int(b)) for (a,b) in [a.split('-') for a in f.read().strip().split(',')]]

running_sum = 0

# I liked my part one answer (commented out), but it was not well fitted to adapt to part two.
for a,b in ranges:
    prev=set()
    for n in range(a,b+1):
        stern = str(n)
        for i in range(1,len(stern)//2 + 1):
            reps = stern[:i]*(len(stern)//i)
            if stern == reps and reps not in prev:
                running_sum+=int(reps)
                prev.add(reps)

'''
for a,b in ranges:
    #note that it is impossible to have a pair of duplicated digits on odd digit counts
    a_digits = math.floor(math.log10(a)) + 1
    if a_digits % 2 : 
        a = 10**a_digits
        a_digits+=1
        if a>b:
            continue

    stra, strb = str(a),str(b) 
    a_start=int(stra[:a_digits // 2])
    
    #lower bounds catch
    if a_start<int(stra[a_digits//2:]):
        a_start+=1

    while a_start*10**(math.floor(math.log10(a_start)) + 1) + a_start <= b:
        running_sum+=a_start*10**(math.floor(math.log10(a_start)) + 1) + a_start
        a_start+=1
'''
print(running_sum)


