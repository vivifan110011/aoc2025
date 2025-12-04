import itertools

with open('./inputs/04_input.txt') as f:
     layout = f.read().strip().split('\n')

layout = [list(l) for l in layout]
xmax, ymax, movable, tm = len(layout[0]), len(layout), 0 , 0

while True:
    layout_new = layout[:]
    for y, x in itertools.product(range(ymax),range(xmax)):
        if layout[y][x] != '@':
            continue

        rollcount=0
        for xmut, ymut in itertools.product(range(-1,2),range(-1,2)):
            #skip self
            if not xmut and not ymut:
                #print(f'\tskip {x+xmut,y+ymut}')
                continue
            #skip edges
            elif x+xmut <0 or x+xmut==xmax or y+ymut<0 or y+ymut==ymax:
                #print(f'\tboundcatch {x+xmut,y+ymut}')
                continue
            if layout[y+ymut][x+xmut]=='@':
                rollcount+=1
        if rollcount<4:
            movable+=1
            layout_new[y][x] = '.'
    
    if not movable:
        break
    
    tm+=movable
    layout, movable = layout_new, 0

print(tm)
