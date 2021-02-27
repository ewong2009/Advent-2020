from node import Node
if __name__ == "__main__" : 
    # Input Parsing
    l = open("input.txt").read()
    d = {}
    for line in l:
        x = int(line)
        d[x] = Node(x, None)       
    for i, line in enumerate(l):
        x = int(line)
        if i == len(l)-1:
            y = int(l[0])
        else:
            y = int(l[i+1])
        d[x].next = d[y]            
    current = d[int(l[len(l)-1])]  
    
    for i in range(0,100):
        #find current node
        current = current.next
        #take out next three nodes
        start = current.next
        end = start.next.next
        #connect current node to fourth node
        current.next = end.next
        temp = [start.value, start.next.value, end.value]     
        #find destination
        destination = (current.value - 2) % len(l) + 1
        while destination in temp:
            destination = (destination - 2) % len(l) + 1
        
        end.next = d[destination].next
        d[destination].next = start
    
    currentNode = d[1].next
    for i in range(len(l)-1):
        print(currentNode.value,end='')
        currentNode = currentNode.next                                                        