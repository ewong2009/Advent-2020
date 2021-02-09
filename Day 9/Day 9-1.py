# This function returns true if two numbers inside nums adds up to total
def TwoSum(nums, total):
    d = {}
    for num in nums:
        if num in d:
            return True
        else:
            d[total - num] = num
    return False
    
if __name__ == "__main__" :
    l = open("input.txt").readlines()
    preamble = 25
    check = [int(l[i]) for i in range(preamble)]
    
    for i in range (preamble,len(l)):
        num = int(l[i])
        if not TwoSum(check,num):
            break
        check.pop(0)
        check.append(num)   
        
    print(num)
    
                    
        
  
        
            
            