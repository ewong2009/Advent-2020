def findBags(d, colour):
    # Base case, if the colour contains no other bags, return 0
    if not d[colour]:
        return 0
    # Otherwise, for each bag add its amount to the total and recurse
    total = 0
    for name, numBags in d[colour]:
        total = total + numBags + findBags(d,name) * numBags
    return total

if __name__ == "__main__" :
    l = open("input.txt").readlines()
    bagDict = {}
    
    for line in l:
        # Input parsing - store bag name and the set of bags they contain in dictionary
        name, b = line.split(" bags contain ")
        b = b.replace("bags","").replace("bag","").replace(".","").replace(" \n","").split(" , ")
        bags = set()          
    
        for item in b:
            if item[0] != 'n':
                bags.add ((item[2:],int(item[0])))

        bagDict[name] = bags

    print(findBags(bagDict, "shiny gold"))