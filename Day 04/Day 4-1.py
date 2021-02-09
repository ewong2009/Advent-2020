if __name__ == "__main__" :
    # Input Parsing
    passports = open("input.txt").read().split("\n\n")
    
    numValid = 0 
    for p in passports:
        # Check for neccesary fields
        if 'byr:' in p and 'iyr:' in p and 'eyr:' in p and 'hgt:' in p and 'hcl:' in p and 'ecl:' in p and 'pid:' in p:
            numValid += 1
                        
    print (numValid)
        
    
    