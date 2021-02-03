if __name__ == "__main__":
    #Input parsing
    l = open("input.txt").readlines()
    
    dict = {}
    total = 2020
    found = 0
    for i in range(len(l)):
        # Subtract each number to get new total
        temp = total - int(l[i])
        # 2Sum using new total
        for k in range(len(l)):
            if k != i:
                num = int(l[k])
                if num in dict:
                    found = dict[num] * num * int(l[i])
                    break
                else:
                    dict[temp - num] = num

        if found: break
    print(found)
              



