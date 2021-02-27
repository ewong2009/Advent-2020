from node import Node
if __name__ == "__main__" :  
    # Input Parsing
    l = open("input.txt").read()
    d = {}
    for i,item in enumerate(l):
        x = int(item)
        d[x] = Node(x,None)  
    for i,item in enumerate(l):
        x = int(item)
        if i == len(l)-1:
            y = int(l[0])
        else:
            y = int(l[i+1])
        d[x].next = d[y]   
        
    d[len(l)+1] = Node(len(l) + 1,None)
    d[int(l[len(l)-1])].next = d[len(l)+1] 
    for i in range(len(l) + 2,1000001):
        d[i] = Node(i,None)
        d[i-1].next = d[i]
    # Wrap around
    d[len(d)].next = d[int(l[0])]        
    
    current = d[len(d)]
    
    for i in range(10000000):
        #find current node
        current = current.next
        #take out next three nodes
        start = current.next
        end = start.next.next
        #connect current node to fourth node
        current.next = end.next
        temp = [start.value, start.next.value, end.value]
        #find destination
        destination = (current.value - 2) % len(d) + 1
        while destination in temp:
            destination = (destination - 2) % len(d) + 1
        end.next = d[destination].next
        d[destination].next = start
        
    firstNode = d[1].next
    secondNode = firstNode.next
    print(firstNode.value * secondNode.value)