def FindSeat(high,low,a,b,instr):
    # Base case, with one or two numbers remaining, return specified number
    if (high - low) <= 1:
        if instr == a:
            return low
        else:
            return high
    # Otherwise, recurse with adjusted range based on instructions
    middle = int((high+low)/2)
    if instr[0] == a:
        return FindSeat(middle,low,a,b,instr[1:])
    elif instr[0] == b:
        return FindSeat(high,middle+1,a,b,instr[1:])
    
    
if __name__ == "__main__" :
    # Input Parsing
    l = open("input.txt").readlines()
    passIDs = set()
    
    for item in l:
        # Find row and column for each boarding pass
        finalrow = FindSeat(127,0,'F','B',item[0:7])         
        finalcolumn = FindSeat(7,0,'L','R',item[7:10])
        # Add the boarding pass ID to a set
        passIDs.add(finalrow * 8 + finalcolumn)
   
    # Print highest boarding pass ID     
    print(max(passIDs))
        
           
                
               
            
    
    
    
    
