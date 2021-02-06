if __name__ == "__main__" :
    # Input Parsing
    groups = open("input.txt").read().split("\n\n")
    total = 0
    
    for group in groups:
        # Split group by members
        members = group.split()
        found = set(members[0])
        # Convert each string to a set and find intersect of the members' answers
        for member in members[1:]:
            member = set(member)
            found = found & member        
        total += len(found)
    
    print(total)