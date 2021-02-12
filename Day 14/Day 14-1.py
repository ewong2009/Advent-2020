# Convert int to binary, apply mask, and return result converted back to int
def ConvertMemory(mask, memory):
    m = MaskLength(mask,bin(int(memory))[2:])
    l = []
    for i in range(len(mask)):
        if mask[i] == 'X':
            l.append(m[i])
        else:
            l.append(mask[i])
    x = ''.join(l)
    return int(x,2)

# Add zeroes in front of m to match length of mask                
def MaskLength(mask,m):
    while len(mask) > len(m):
        m = '0' + m
    return m

if __name__ == "__main__" :   
    # Input Parsing
    l = open("input.txt").readlines()
    masks = {}
    for line in l:
        if line[0:4] == "mask":
            key = line.split(" = " )[1].replace('\n','')
            masks[key] = []
        else:
            address, val = line.split(" = ")
            masks[key].append((address[4:-1], val.replace('\n','')))   
   
    # Apply mask to each number and save in memory
    memory = {}
    for key in masks:
        for address, value in masks[key]:
            memory[address] = ConvertMemory(key, value)
       
    total = 0 
    for key in memory:    
        total += memory[key]
    
    print(total)   