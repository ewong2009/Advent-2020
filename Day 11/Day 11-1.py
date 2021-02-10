# Returns whether or not all seats adjacent to l[a][b] are empty
def FillSeat(l, a, b, columns, rows):
    pos = {(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)}
    for x, y in pos:
        x, y = a + x, b + y
        if 0 <= x < rows and 0 <= y < columns and not checkEmpty(l[x][y]):
            return False   
    return True

# Returns whether or not 4 or more seats adjacent to l[a][b] are filled
def EmptySeat(l, a, b, columns, rows):
    pos = {(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)}
    filled = 0
    for x, y in pos:
        x, y = a + x, b + y
        if 0 <= x < rows and 0 <= y < columns and not checkEmpty(l[x][y]):
            filled += 1
            if filled == 4:
                return True
    return False  

# Fills seats in l based on rules and returns number of changes made
def FillSeats(l):
    changes = 0
    columns = len(l[0])
    rows = len(l)
    seatsToFill = set()
    for i in range(rows):
        for k in range(columns):
            if l[i][k] == "L":
                if FillSeat(l, i, k, columns, rows):
                    seatsToFill.add((i,k))
                    changes += 1
    for x,y in seatsToFill:
        l[x][y] = '#'
    return (l,changes)

# Empties seats in l based on rules and returns number of changes made
def EmptySeats(l):
    changes = 0
    columns = len(l[0])
    rows = len(l)
    seatsToEmpty = set()
    for i in range(rows):
        for k in range(columns):
            filled = 0
            if l[i][k] == "#":
                if EmptySeat(l, i, k, columns, rows):
                    seatsToEmpty.add((i,k))
                    changes += 1
    for x,y in seatsToEmpty:
        l[x][y] = 'L'    
    return (l,changes)

# Returns whether or not a seat is empty                            
def checkEmpty(s):
    if s in 'L0.':
        return True
    return False

# Returns the total number of occupied seats
def numOccupied(l):
    total = 0
    columns = len(l[0])
    for line in l:
        total += line.count('#')
    return total
            
if __name__ == "__main__" :
    # Input Parsing
    l = open("input.txt").readlines()   
    for i in range(len(l)):
        l[i] = list(l[i].strip())
    
    # Execute rules until there are no changes
    while True:
        l, changes = FillSeats(l)
        if changes == 0:
            break   
        l, changes = EmptySeats(l)
        if changes == 0:
            break
                    
    print(numOccupied(l))        