from instruction import Instruction

if __name__ == "__main__" :
    # Input Parsing
    l = open("input.txt").readlines()
    instructionList = []
    index = 0
    result = 0
    
    # Input parsing, create a list of Instruction objects
    for line in l:
        instructionList.append(Instruction(line[:3],int(line[4:])))
    
    # Loop through instructions
    while True:
        # Execute instruction and set seen to True
        instructionList[index].seen = True
        instr = instructionList[index]
        if instr.action == "acc":
            result += instr.value
            index += 1
        elif instr.action == "jmp":
            index += instr.value
        else:
            index +=1
        # Break from loop when an index is repeated
        if instructionList[index].seen:
            break
    
    print(result)
        
        
 
    
    
    
    