if __name__ == "__main__":
    
    l = open("input.txt").readlines()
    total = 0
    
    for i in range(len(l)):
        # Input parsing
        min, max, letter, phrase = l[i].replace("-"," ").replace(":","").split()
        count = 0
       
        # Find instances of letter within phrase
        for j in range(len(phrase)):
            if phrase[j] == letter:
                count += 1
            
        if (count >= int(min)) and (count <= int(max)):
            total += 1
    
    print(total)
    

            
