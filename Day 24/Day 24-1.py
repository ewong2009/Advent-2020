if __name__ == "__main__" :
    l = open("input.txt").read().strip().split('\n')
    black = set() 
    move = {'e':(1,0),'w':(-1,0),'ne':(0.5,1),'nw':(-0.5,1),'se':(0.5,-1), 'sw':(-0.5,-1)}
    for line in l:
        x = y = i = 0
        while i < len(line):
            if line[i] in 'ew':
                d = line[i]
                i += 1
            else:
                d = line[i:i+2]
                i += 2         
            x += move[d][0]
            y += move[d][1]
            
        # Find symmetric difference of black and coord
        black = black ^ {(x,y)}         
    
    print(len(black))