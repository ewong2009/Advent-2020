if __name__ == "__main__" :
    # Input Parsing
    initialTime, Busses = open("input.txt").readlines()
    Busses = [int(i) for i in Busses.split(',') if i != 'x']
    initialTime = int(initialTime)
    earliestBus = Busses[0]
    time =  Busses[0] - initialTime % Busses[0]
    
    for bus in Busses[1:]:
        if bus - (initialTime % bus) < time:
            earliestBus = bus
            time = bus - (initialTime % bus)
       
    print(earliestBus * time)