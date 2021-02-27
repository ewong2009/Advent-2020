if __name__ == "__main__" :  
    l = open("input.txt").read().strip().split('\n') 
    black = set()
    move = {'e':(1,0),'w':(-1,0),'ne':(0.5,1),'nw':(-0.5,1),'se':(0.5,-1), 'sw':(-0.5,-1)}
    for item in l:
        x = y = i = 0 
        while i < len(item):
            if item[i] == 'e' or item[i] == 'w':
                d = item[i]
                i+=1
            else:
                d = item[i:i+2]
                i+=2         
            x += move[d][0]
            y += move[d][1]       
        # Find symmetric difference of black and coord
        black = black ^ {(x,y)}            
    
    # Find each tile's adjacent black and white tiles, and make changes accordingly - repeat for 100 cycles 
    for i in range(100):     
        blackAdj = {}
        whiteAdj = {}
        for item in black:
            x = item[0]
            y = item[1]
            adj = [(x+1, y),(x-1, y),(x+0.5, y+1),(x-0.5, y+1),(x+0.5, y-1), (x-0.5, y-1)]
            for tile in adj:
                if tile in black:
                    if tile in blackAdj:
                        blackAdj[tile] += 1
                    else:
                        blackAdj[tile] = 1
                else:
                    if tile in whiteAdj:
                        whiteAdj[tile] += 1
                    else:
                        whiteAdj[tile] = 1
        black = set()
        for item in whiteAdj:
            if whiteAdj[item] == 2:
                black.add(item)        
        for item in blackAdj:
            if 0 < blackAdj[item] < 3:
                black.add(item)
                       
    print(len(black))