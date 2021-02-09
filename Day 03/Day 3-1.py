if __name__ == "__main__" :
    # Input Parsing
    l = open("input.txt").readlines()
   
    # Initialize variables
    length = len(l[0])-1;
    x = 0
    totaltrees = 0
    
    # Travel down the map
    for i in range(len(l)-1):
        # Use mod for wrapping
        x = (x + 3) % length
        if l[i+1][x] == '#':
            totaltrees += 1
    
    print (totaltrees)
           
        
        