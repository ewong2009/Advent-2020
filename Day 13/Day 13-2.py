if __name__ == "__main__" :   
    # Input Parsing
    _ , Busses = open("input.txt").readlines()
    Busses = [[int(bus),i] for i,bus in enumerate(Busses.split(',')) if bus != 'x']
    initialTime = 0
    difference = Busses[0][0]

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