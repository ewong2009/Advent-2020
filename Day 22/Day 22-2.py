# Plays a game of Recursive Combat and returns the winner's deck
def Play(player1, player2):
    cache = set()
    # Continue playing while neither deck is empty
    while len(player1) > 0 and len(player2) > 0:
        # Check for infinite loop
        tuple1 = tuple(player1)
        tuple2 = tuple(player2) 
        if (tuple1,tuple2) in cache:
            return 1
        # Add decks into the cache
        cache.add((tuple1,tuple2))     
        num1 = player1.pop(0)
        num2 = player2.pop(0)
        
        # Determine winner of the round, if either card is larger than the size
        # of a player's deck, higher card wins the round
        if num1 > len(player1) or num2 > len(player2):
            if num1 > num2:
                result = 1
            else:
                result = 0
        # Otherwise, make a copy of the decks and recurse to find the winner of the round
        else:
            copy1 = player1[0:num1]
            copy2 = player2[0:num2]  
            result = Play(copy1, copy2)        
        # Add cards to winner's deck      
        if result:
            player1.append(num1)
            player1.append(num2)
        else:
            player2.append(num2)
            player2.append(num1)      
    # Determine the winner      
    if not len(player1):
        return 0
    return 1
    
if __name__ == "__main__" :   
    # Input parsing
    l = open("input.txt").read().strip().split("\n\n")
    player1 = [int(item) for i, item in enumerate(l[0].split("\n")) if i != 0]
    player2 = [int(item) for i, item in enumerate(l[1].split("\n")) if i != 0]   
        
    # Play game, find winner, and calculate score
    if Play(player1, player2):
        winner = player1
    else:
        winner = player2
   
    total = 0
    winner.reverse()
    for i,item in enumerate(winner):
        total += (i+1) * item
  
    print(total)