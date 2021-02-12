if __name__ == "__main__" :   
    # Input Parsing
    nums = open("input.txt").read().split(',')
    spoken = {}
    for i in range(len(nums)-1):
        spoken[int(nums[i])] = i 
    lastNum = int(nums[len(nums)-1])
    
    # Loop through 2020 turns following  the rules of the game
    for i in range(len(nums)-1,2019):
        if lastNum in spoken:
            temp = lastNum
            lastNum = i - spoken[lastNum]
            spoken[temp] = i
        else:
            spoken[lastNum] = i
            lastNum = 0
    
    print (lastNum)