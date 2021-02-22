# Tile object which contains its four sides
class Tile:
    def __init__(self, name, top, bottom, left, right):
        self.name = name
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
    
    def display(self):
        print(self.name,self.top,self.bottom,self.left,self.right)

# Tile object which contains its full grid and its four sides 
class fullTile:
    def __init__(self, name, grid):
        self.name = name
        self.grid = grid
        self.update()
    
    def display(self):
        print(self.name,self.grid)
    
    def displaySides(self):
        print("t:",self.top,"b:",self.bottom,"l:",self.left,"r:",self.right)
    
    # Updates the sides for a tile whenever its orientation is changed
    def update(self):
        self.top = self.grid[0]
        self.bottom = self.grid[len(self.grid)-1]
        self.left = [s[0] for s in self.grid]
        self.right = [s[-1] for s in self.grid]   
    
    # Rotates tile 90 degrees
    def rotate(self):
        self.grid = rotate(self.grid)
        self.update()
    
    # Flips tile by its bottom edge   
    def flip(self):
        self.grid = flip(self.grid)
        self.update()

# Returns grid rotated to the right 90 degrees        
def rotate(grid):
    temp = []
    length = len(grid)
    for i in range(length):
        row = ""
        for j in range(length - 1,-1,-1):
            row += grid[j][i]
        temp.append(row)
    grid = temp
    return grid

# Returns grid flipped on its bottom edge
def flip(grid):
    temp = []
    length = len(grid)
    for i in range(length -1, -1,-1):
        temp.append(grid[i])
    grid = temp
    return temp
     