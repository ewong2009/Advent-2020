from instruction import Instruction

def instrEnds(instructions,i,r): 
    # Loop through instructions
    while True:
        # Execute instruction and set seen to True
        instructions[i].seen = "True"
        if instructions[i].action == "acc":
            r += instructions[i].value
            i += 1
        elif instructions[i].action == "jmp":
            i += instructions[i].value
        else:
            i += 1
        # Return 0 if an index is repeated
        if instructions[i].seen:
            return 0
        # Return result if the last index is reached
        if i == len(instructions)-1:
            return r
               
# Change action from 'nop' to 'jmp' and vice versa
def swap(instr):
    if instr.action == "nop":
        return "jmp"
    elif instr.action == "jmp":
        return "nop"
    
if __name__ == "__main__" :
    # Input Parsing
    l = open("input.txt").readlines()
    instructionList = []
    i = 0
    result = 0
    
    # Input parsing, create a list of Instruction objects
    for line in l:
        instructionList.append(Instruction(line[:3],int(line[4:])))
        
    # Loop through the instructions, starting with instruction 0
    while True:
        # Change seen value to True 
        instructionList[i].seen = "True"
        if instructionList[i].action == "acc":
            result += instructionList[i].value
            i += 1
        else:
            # If action is 'nop' or 'jmp', swap and try to reach the last index
            instructionList[i].action = swap(instructionList[i])
            answer = instrEnds(instructionList, i, result)
            # If it does not end, swap the value back and execute instructions
            if not answer:
                instructionList[i].action = swap(instructionList[i])
                if instructionList[i].action == "nop":
                    i += 1
                elif instructionList[i].action == "jmp":
                    i += instructionList[i].value
            # Otherwise, the answer is found - break from loop
            else:
                break
     
    print(answer)         
                
        
            
        
        
        
        