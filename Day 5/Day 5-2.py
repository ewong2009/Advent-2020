def FindMissing(s): 
    # Check each ID from smallest to largest to find the missing pass ID
    for i in range(min(s), max(s)):
        if i not in s:
            return i

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
    l = open("input.txt","r").readlines()
    passIDs = set()
    
    for item in l:
        # Find row and column for each boarding pass
        row = FindSeat(127,0,'F','B',item[0:7])         
        column = FindSeat(7,0,'L','R',item[7:10])
        # Add the boarding pass ID to a set
        passIDs.add(row * 8 + column)
   
    # Find the missing number within the IDs
    print(FindMissing(passIDs)) 
    
      
    
    
    
    