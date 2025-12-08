import itertools

with open('./inputs/05_input.txt') as f:
    iterable=f.read().strip().splitlines()

ranges, ids = [], []
rangemaker = lambda a,b: range(int(a),int(b)+1)
normalranges=[]

for v, term in enumerate(iterable):
    if not term:
        ids = iterable[v+1:]
        break

    ranges.append(rangemaker(*term.split('-')))
    normalranges.append(list(map(int,term.split('-'))))

rs=0
for item in ids:
    if any(int(item) in r for r in ranges):
        rs+=1

print(rs)

#Take a list of ranges and isolate the virst value as `a`.
# Iterate through `rest` checking if expansion of any range is possible
# If expansion is possible, modify `rest` in place @ idx and return modified `rest`.
# If nothing is returned from coalesce, `a` had no overlaps with any member of `rest`, and as such is a static member of the final list of ranges.
# a -> modified rest @ idx 0, rest = modified rest @ idx 1->
# Repeat until `rest` is exhausted.

def coalesce(a,rest):
    for idx, nr in enumerate(rest):
        if (a[0] <= nr[0] and a[1] >= nr[0]-1) or (a[0] <= nr[1]+1 and a[1] >= nr[1]):
            rest[idx][0]=min(a[0], nr[0])
            rest[idx][1]=max(a[1], nr[1])
            return rest

normalranges.sort()
finalized = []
a,rest = normalranges[0], normalranges[1:]

while rest:
    ret = coalesce(a,rest)
    if not ret:
        finalized.append(a)
    a, rest = ret[0] if ret else rest[0], ret[1:] if ret else rest[1:]
        
finalized.append(a)
items = 0
for term in finalized:
    items+=(term[1]-term[0] + 1)


print(items)
