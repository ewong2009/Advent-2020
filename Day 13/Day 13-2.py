if __name__ == "__main__" :   
    # Input Parsing
    Busses = [(int(bus),i) for i,bus in enumerate(open("input.txt").readlines()[1].split(',')) if bus != 'x']
    initialTime, difference = 0, Busses[0][0]

    ''' Find the first time which works for the first two busses, then add the third bus, 
        fourth, etc. until you find a time which works with every bus '''
    for busNo, change in Busses[1:]:
        found = False
        while not found:
            initialTime = initialTime + difference
            busArrival = initialTime + change
            if busArrival % busNo == 0:
                difference = difference * busNo
                found = True
                
    print(initialTime)              