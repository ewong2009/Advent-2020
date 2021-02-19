import copy
# Returns the number of active cubes adjacent to l[z][y][x]
def validNeighbours(l,z,y,x):
    total = 0
    zSize, ySize, xSize = len(l), len(l[0]), len(l[0][0])
    for i in range(z-1,z+2):
        for j in range(y-1,y+2):
            for k in range(x-1,x+2):
                if 0 <= i < zSize and 0 <= j < ySize and 0 <= k < xSize and l[i][j][k] and (z!=i or y!=j or x!=k) and l[i][j][k] == "#":
                    total += 1
                    if total > 3:
                        return total
    return total

# Returns the number of active cubes in l
def FindActive(l):
    total = 0
    zSize, ySize, xSize = len(l), len(l[0]), len(l[0][0])
    for z in range(zSize):
        for y in range(ySize):
            for x in range(xSize):
                if l[z][y][x] == '#':
                    total += 1
    return total

if __name__ == "__main__" :   
    # Input Parsing
    l = [list(n.replace('\n','')) for n in open("input.txt").readlines()]
    # Create model representation
    zSize = 12
    xSize = ySize = len(l) + 12
    zMid = int(zSize/2)
    yMid = int(ySize/2) - int(len(l)/2)
    xMid = int(xSize/2) - int(len(l[0])/2)       
    model = []  
    for z in range(zSize):
        ys = []
        for y in range(ySize):
            xs = []
            for x in range(xSize):
                xs.append('.')
            ys.append(xs)
        model.append(ys)                    
    
    for i,item in enumerate(l):
        for j in range(len(item)):
            model[zMid][yMid + i][xMid + j] = l[i][j]
   
    # Execute rules 6 cycles
    for i in range(6):
        temp = copy.deepcopy(model)
        for z in range(zSize):
            for y in range(ySize):
                for x in range(xSize):
                    nums = validNeighbours(model,z,y,x)                   
                    if model[z][y][x] == '.' and nums == 3:
                        temp[z][y][x] = '#'
                    elif model[z][y][x] == '#' and not(1 < nums < 4):
                        temp[z][y][x] = '.'                                                          
        model = temp   
    
    print(FindActive(model))