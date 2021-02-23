if __name__ == "__main__" :   
    # Input parsing
    l = open("input.txt","r").read().strip().split("\n\n")
    player1 = [int(item) for i, item in enumerate(l[0].split("\n")) if i != 0]
    player2 = [int(item) for i, item in enumerate(l[1].split("\n")) if i != 0]   
    
    # Continue to play game while neither deck is empty
    while len(player1) > 0 and len(player2) > 0:
        num1 = player1.pop(0)
        num2 = player2.pop(0)
        # Player with higher card gets both cards
        if num1 > num2:
            player1.append(num1)
            player1.append(num2)
        elif num2 > num1:
            player2.append(num2)
            player2.append(num1)
     
    # Find winner and calculate score    
    if player1:
        winner = player1
    else:
        winner = player2   
    total = 0  
    winner.reverse()
    for i,item in enumerate(winner):
        total += (i+1) * item  
    print(total)                    