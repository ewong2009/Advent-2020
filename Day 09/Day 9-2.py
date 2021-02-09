# Returns true if two numbers inside nums adds up to total
def TwoSum(nums, total):
    d = {}
    for num in nums:
        if num in d:
            return True
        else:
            d[total - num] = num
    return False

# Returns a range of numbers in l which add up to total
def Find(l,total):
    # Loops through each possible size of range, and finds the sum
    for i in range(2,len(l)):
        s = 0
        for j in range(i):
            s += int(l[j])          
        for j in range(i,len(l)):
            if s == total:
                return l[j-i:j]
            s += int(l[j])
            s -= int(l[j-i])
                
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
    
    x = Find(l,num)
    print(int(max(x)) + int(min(x)))
        