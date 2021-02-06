if __name__ == "__main__" :
    # Input Parsing
    groups = open("input.txt").read().split("\n\n")
    total = 0

    for group in groups:
        # Convert each string to set and drop the newline character 
        group = set(group)
        group.discard('\n')
        total += len(group)
    
    print(total)