# Returns coordinates after moving ship in direction of waypoint by given units
def Move(coord, units, waypoint):
    return [coord[0] + waypoint[0] * units, coord[1] + waypoint[1] * units]
    
# Returns waypoint after movement
def MoveWaypoint(waypoint, direction, units):   
    if direction == 'N':
        waypoint[1] += units
    elif direction == 'S':
        waypoint[1] -= units
    elif direction == 'E':
        waypoint[0] += units
    elif direction == 'W':
        waypoint[0] -= units
    return waypoint

# Returns waypoint after rotation 
def ChangeDirection(units, direction, wp):
    if units == 180:
        wp = [-wp[0], -wp[1]]
    else:  
        if direction == 1:
            if units == 90:
                wp = [wp[1], -wp[0]]
            elif units == 270:
                wp = [-wp[1], wp[0]]
        else:
            if units == 90:
                wp = [-wp[1], wp[0]]
            elif units == 270:
                wp = [wp[1], -wp[0]]
    return wp   
    
if __name__ == "__main__" :
    # Input Parsing
    instructions = [[l[0], int(l[1:])] for l in open("input.txt").readlines()]
    XYloc = [0,0]
    waypoint = [10,1]

    for command, units in instructions:
        if command == "F":
            XYloc = Move(XYloc, units, waypoint)
        elif command == "L":
            waypoint = ChangeDirection(units, -1, waypoint)
        elif command == "R":
            waypoint = ChangeDirection(units, 1, waypoint)
        else:
            waypoint = MoveWaypoint(waypoint,command,units)
    
    print(abs(XYloc[0]) + abs(XYloc[1]))
