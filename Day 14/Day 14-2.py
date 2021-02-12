# Returns a list of addresses created by applying mask to memory
def ConvertMemory(mask, memory):
    m = MaskLength(mask,bin(int(memory))[2:])
    l = [[]]
    for i in range(len(mask)):
        if mask[i] == "0":
            for item in l:
                item.append(m[i])                   
        elif mask[i] == "1":
            for item in l:
                item.append("1")               
        elif mask[i] == "X":
            for j in range(len(l)):
                l.append(l[j] + ["1"])
                l[j].append("0")               
    for i in range(len(l)):
        l[i] = "".join(l[i])
        l[i] = int(l[i],2)            
    return l

# Add zeroes in front of m to match length of mask    
def MaskLength(mask,m):
    while(len(mask) > len(m)):
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
    print(masks)
    # Apply mask to each address and save value in memory
    memory = {}
    for key in masks:
        for address, value in masks[key]:
            temp = ConvertMemory(key,address)
            for t in temp:
                memory[t] = int(value)
   
    total = 0
    for key in memory:
        total += memory[key]
    
    print(total)