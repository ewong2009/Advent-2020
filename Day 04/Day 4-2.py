import re
def Verify(code, info):
 
    # Verify information based on code
   
    # Birth year
    if code == 'byr':
        if not (int(info) >= 1920 and int(info) <= 2002):
            return False
   
    # Issue year       
    elif code == 'iyr':
        if not (int(info)>= 2010 and int(info) <= 2020):
            return False
   
    # Expiry year    
    elif code == 'eyr':
        if not (int(info) >= 2020 and int(info) <= 2030):
            return False
   
    # Height
    elif code == 'hgt':
        if info[-2:] == 'in': 
            if not (int(info[:-2]) >= 59 and int(info[:-2]) <= 76):
                return False 
        elif info[-2:] == 'cm':
            if not (int(info[:-2]) >= 150 and int(info[:-2]) <= 193):
                return False 
        else:
            return False
   
    # Hair Colour    
    elif code == 'hcl':
        if not re.match("^#[a-f0-9]{6}$",info):
            return False
   
    # Eye Colour
    elif code == 'ecl':
        if not info in ["amb" ,"blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
  
    # Passport ID
    elif code == 'pid':
        if not re.match("^0*[0-9]{9}$",info):
            return False
        
    # Return true if no rules are broken
    return True   

if __name__ == "__main__" :
    # Input Parsing
    passports = open("input.txt").read().split('\n\n')
    numValid = 0
    
    for p in passports:
        # Check for neccesary fields
        if 'byr:' in p and 'iyr:' in p and 'eyr:' in p and 'hgt:' in p and 'hcl:' in p and 'ecl:' in p and 'pid:' in p:
            items = p.replace('\n',' ').split()
            # Verify each field
            for item in items:
                code = item[:3]
                info = item[4:]
                if not Verify(code, info):
                    break
            else:
                numValid += 1
        
    print (numValid)