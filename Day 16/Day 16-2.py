from copy import deepcopy
if __name__ == "__main__" :   
    # Input Parsing
    x, y, z = open("input.txt").read().replace("nearby tickets:\n","").replace("your ticket:\n","").strip().split("\n\n")
    x, myTicket, z = x.split('\n'), y.split(','), z.split('\n')
    fields, names = {}, set()
    for line in x:
        name, nums = line.split(': ')
        a,b,c,d = nums.replace(' or ',' ').replace('-',' ').split()
        fields[name] = (int(a),int(b),int(c),int(d))
        names.add(name)    
    tickets = [[int(i) for i in line.split(',')] for line in z]

    # Find invalid tickets
    invalid = []
    for i, ticket in enumerate(tickets):
        for num in ticket:
            for a,b,c,d in fields.values():
                if (a <= num <= b) or (c <= num <= d):
                    break
            else:
                invalid.append(i)
                
    # Remove invalid tickets     
    invalid = sorted(invalid, reverse = True)
    for item in invalid:
        tickets.pop(item)
    
    # Find the possible fields for each index
    validFields = []
    for i in range(len(fields)):
        validFields.append([i, deepcopy(names)])  
    for ticket in tickets:
        for j, num in enumerate(ticket):
                for key, val in fields.items():
                    if (num < val[0] or num > val[1]) and (num < val[2] or num > val[3]):
                        validFields[j][1].discard(key)

    # Assign index to each field by process of elimination
    validFields.sort(key = lambda x: x[1])
    fieldIndex = {}
    for i, fields in validFields:
        for field in fields:
            if field not in fieldIndex:
                fieldIndex[field] = i
    
    # Calculate answer using my ticket            
    total = 1
    for key in fieldIndex:
        if "departure" in key:
            total = total * int(myTicket[fieldIndex[key]])
    
    print(total)