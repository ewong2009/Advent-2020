if __name__ == "__main__" :
    # Input parsing
    nums = sorted([int(i) for i in open("input.txt").readlines()])
    threes = 1 # for connection at the end
    ones = 1   # for connection at the start
    twos = 0
    
    for i,num in enumerate(nums[1:]):
        if num - nums[i] == 1:
            ones += 1
        elif num - nums[i] == 3:
            threes += 1
        else:
            twos +=1

    print (threes*ones)
        
    