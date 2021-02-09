if __name__ == "__main__" :
    # Input parsing
    nums = sorted([int(i) for i in open("input.txt").readlines()])
   
    # Insert 0 at start and the largest number + 3 at the end of the list
    nums.append(nums[len(nums)-1] + 3)
    nums.insert(0,0)
    
    # Solve using dynamic programming
    paths = [0] * len(nums)
    paths[0] = 1
    for i in range(1,len(nums)):
        for j in range(i-1,i-4,-1):
            if j < 0:
                break
            if nums[i] - nums[j] <= 3:
                paths[i] += paths[j]
    
    print(paths[len(nums)-1])