if __name__ == "__main__":
    
    l = open("input.txt","r").readlines()
    total = 0
    
    for i in range(len(l)):
        # Input parsing
        first, second, letter, phrase = l[i].replace("-"," ").replace(":","").split()
        
        # Check the given positions for the letter
        if phrase[int(first)-1] == letter and phrase[int(second)-1] != letter:
            total+=1
        elif phrase[int(second)-1] == letter and phrase[int(first)-1] != letter:
            total+=1
            
            
    print(total)