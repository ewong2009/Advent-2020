from tile import Tile

# Returns whether or not t1 and t2 have any matching sides
def Compare(t1,t2):
    first = {t1.top, t1.bottom, t1.left, t1.right}
    second = {t2.top, t2.bottom, t2.left, t2.right}        
    for side in first:
        rev = list(side)
        rev.reverse()
        rev = tuple(rev)
        if side in second or rev in second:
            return True        
    return False

if __name__ == "__main__" :   
    # Input Parsing
    l = open("input.txt").read().split("\n\n")
    tiles = []   
    for item in l:
        temp = item.split("\n")
        name = int(temp[0][5:9])
        top = tuple(temp[1])
        bot = tuple(temp[len(temp)-1])
        left = []
        right = []
        for i in range(1,len(temp)):
            left.append(temp[i][0])
            right.append(temp[i][len(temp[i])-1])
        tiles.append(Tile(name, top, bot, tuple(left), tuple(right)))
    
    # Find 4 corners by finding tiles which only fit with two other tiles    
    corners = []     
    for item in tiles:
        matching = 0
        for comp in tiles:
            if item != comp:
                if Compare(item,comp):
                    matching += 1 
                if matching > 2:
                    break
        else:
            corners.append(item)
             
    answer = 1
    for item in corners:
        answer *= item.name  
    print(answer)    