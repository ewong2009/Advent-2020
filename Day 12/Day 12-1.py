# Returns coordinates after moving ship in specified direction by given units
def Move(coord, direction, units):
    if direction == 0:
        coord[0] += units
    elif direction == 1:
        coord[1] -= units
    elif direction == 2:
        coord[0] -= units
    else:
        coord[1] += units
    return coord

# Returns direction the ship is facing after rotation
def ChangeDirection(direction, units, move):
    return (direction + move * units) % 4
        
if __name__ == "__main__" :
    # Input Parsing - E:0, S:1, W:2, N:3
    instructions = [[l[0],int(l[1:].strip())] for l in open("input.txt").read().replace('E','0').replace('S','1').replace('W','2').replace('N','3').split()]
    XYloc = [0,0]
    currentDir = 0
    for command, units in instructions:
        if command == "F":
            XYloc = Move(XYloc, currentDir, units)
        elif command == "L":
            currentDir = ChangeDirection(currentDir, int(units/90), -1)
        elif command == "R":
            currentDir = ChangeDirection(currentDir, int(units/90), 1)
        else:
            XYloc = Move(XYloc, int(command), units)
    
    print(abs(XYloc[0]) + abs(XYloc[1]))
            