def findBags(d, colour):
    found = set()
    # Check each bag for the colour we're looking for
    for name in d:
        # If found, add bag to set and recurse
        if colour in d[name]:
            found.add(name)
            found = found | findBags(d,name)
    return found

if __name__ == "__main__" :
    l = open("input.txt").readlines()
    bagDict = {}
 
    for line in l:
        # Input parsing - store bag name and the set of bags it contains in dictionary
        name, b = line.split(" bags contain ")
        b = b.replace("bags","").replace("bag","").replace(".","").replace(" \n","").split(" , ")
        bags = set()
        for item in b:
            bags.add(item[2:])
        bagDict[name] = bags
        
    print(len(findBags(bagDict,"shiny gold")))