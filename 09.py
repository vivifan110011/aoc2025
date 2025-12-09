import numpy as np

with open('inputs/09_input.txt') as f:
    lines = f.read().strip().splitlines()
    lines = [tuple(map(int,y.split(','))) for y in lines]

LOW_X, LOW_Y = float('inf'), float('inf')
HIGH_X, HIGH_Y = float('-inf'), float('-inf')

for coord in lines:
    LOW_X, LOW_Y = min(LOW_X, coord[1]), min(LOW_Y, coord[0])
    HIGH_X, HIGH_Y = max(HIGH_X, coord[1]), max(HIGH_Y, coord[0])


max_area = float('-inf')
square_calc = lambda a,b: (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1])+1)

for i in range(len(lines)-1):
    #print(lines[i])
    for j in range(i+1,len(lines)):
        #print('\t',lines[j], square_calc(lines[i],lines[j]))
        max_area = max(square_calc(lines[i],lines[j]),max_area)


print('p1', max_area)
   

#This.. could be quite slow.
#pathing
grid = np.zeros((HIGH_X + 1,HIGH_Y+1), dtype=np.bool_)
lc = lines[0]
for coord in lines[1:] + [lc]:
    if coord[0] - lc[0]:
        grid[coord[1],min(coord[0],lc[0]):max(coord[0],lc[0]) + 1] = True
    else:
        grid[min(coord[1],lc[1]):max(coord[1],lc[1]) + 1,coord[0]] = True
    lc = coord

for i in range(len(grid)):
    res = np.where(grid[i] == True)
    if res[0].any():
        grid[i,res[0][0]:res[0][-1]+1] = True

max_area=float('-inf')
for i in range(len(lines)-1):
    for j in range(i+1,len(lines)):
        ymin, ymax = min(lines[i][1],lines[j][1]), max(lines[i][1],lines[j][1])  
        xmin, xmax = min(lines[i][0],lines[j][0]), max(lines[i][0],lines[j][0]) 
        # :)
        if not np.any(grid[ymin:ymax+1,xmax] == False) and not np.any(grid[ymin:ymax+1,xmin] == False) and not np.any(grid[ymax,xmin:xmax+1] == False) and not np.any(grid[ymin,xmin:xmax+1] == False):
            max_area = max(square_calc(lines[i],lines[j]),max_area)
            
print('p2', max_area)


