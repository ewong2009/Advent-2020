def findTrees(right,down,l):
      totaltrees = 0
      x = 0
      y = 0
      # Travel down map using directions, finding all trees along the way
      while y<len(l)-1:
            # Mod for wrapping
            x = (x + right) % (len(l[y])-1)
            y += down
            if l[y][x] == '#':
                  totaltrees += 1
                  
      return totaltrees

if __name__ == "__main__" :
      # Input parsing
      l = open("input.txt").readlines()
      
      # Calculate the total number of trees 
      print (findTrees(1,1,l) * findTrees(3,1,l) * findTrees(5,1,l) * findTrees(7,1,l) * findTrees(1,2,l))
     