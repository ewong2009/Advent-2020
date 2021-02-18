if __name__ == "__main__" :  
    # Input Parsing
    fields, _, nTix = open("input.txt").read().replace("nearby tickets:\n","").strip().split("\n\n")
    fields = fields.split("\n")
    ranges = []
    for line in fields:
        first, second = line.split(":")[1].split(" or ")
        first = first.split("-")
        second = second.split("-")
        ranges.append([int(first[0]),int(first[1])])
        ranges.append([int(second[0]),int(second[1])])   
    nTix = nTix.replace("\n",",")
    tickets = [int(i) for i in nTix.split(',')]
         
    # Find invalid tickets and add their values to total    
    total = 0
    for ticket in tickets:
        for low, high in ranges:
            if low <= ticket <= high:
                break
        else:
            total += ticket
            
    print(total)
    
        