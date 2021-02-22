from tile import fullTile
from tile import flip
from tile import rotate
from math import sqrt

# Recursive function which finds the positions of each tile to fit inside the board
# Find an empty spot on the board, if there are no spots left, board is completely solved - returns True 
# Otherwise place a tile in the empty spot and continue to solve
def Solve(board, tiles): 
    place = FindEmpty(board)
    if not place:
        return True
    x = place[0]
    y = place[1]
    for i in range(len(tiles)):
        tile = tiles[0]
        tiles.remove(tile)
        count = 0
        while count < 8:
            if IsValid(tile, board, x, y):
                board[x][y] = tile
                if Solve(board,tiles):
                    return True
                board[x][y] = 0
            count += 1
            if count == 4:
                tile.flip()
            tile.rotate()
        tiles.append(tile)
    return False

# Returns whether or not the tile would be valid in position x,y on the board           
def IsValid(tile, board, x, y):
    if x > 0:
        if board[x-1][y].bottom != tile.top:
            return False
    if y > 0:
        if board[x][y-1].right != tile.left:
            return False        
    return True

# Returns the first empty spot found on the board
def FindEmpty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return [i,j]
    return False

# Returns the number of sea monsters found on the picture
def FindMonsters(pic):
    found = 0
    length = len(pic)
    indices = {(1,-18),(1,-13),(1,-12),(1,-7),(1,-6),(1,-1),(1,0),(1,1),(2,-17),(2,-14),(2,-11),(2,-8),(2,-5),(2,-2)}
    for i in range(length-3):
        for j in range(17,length-1):
            if pic[i][j] == '#':
                for x,y in indices:
                    if pic[x + i][y + j]!= '#':
                        break
                else:
                    found += 1    
    return found

if __name__ == "__main__" : 
    # Input Parsing
    l = open("input.txt").read().split("\n\n")
    tiles = []    
    for line in l:
        temp = line.split("\n")
        name = int(temp[0][5:9])
        grid = []
        for i in range(1,len(temp)):
            grid.append(temp[i])
        tiles.append(fullTile(name, grid))
    
    # Initialize solution grid with zeroes
    side = int(sqrt(len(tiles)))  
    solution = []
    for i in range(side):
        row = []
        for j in range(side):
            row.append(0)
        solution.append(row)
    
    # Solve grid    
    x = Solve(solution,tiles)
       
    # Put picture together and remove sides
    size = len(solution[0][0].grid)
    pic = []
    for i in range(side):
        for j in range(1,size-1):
            row = ''
            for k in range(side):
                row += solution[i][k].grid[j][1:-1]
            pic.append(row)
       
    for i in range(8):
            numMonsters = FindMonsters(pic)
            if numMonsters > 0:
                break
            pic = rotate(pic)
            if i == 3:
                pic = flip(pic)
     
    # Calculate the total number of hashtags remaining after removing sea monsters
    totalHashtags = 0
    length = len(pic)
    for i in range(length):
        for j in range(length):
            if pic[i][j]=='#':
                totalHashtags += 1
    
    print(totalHashtags - numMonsters * 15)