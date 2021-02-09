if __name__ == "__main__":
    #Input parsing
    l = open("input.txt").readlines()
    
    # Use dictionary to store the compliment of each number
    dict = {}
    total = 2020
    for i in range(len(l)):
        num = int(l[i])
        if num in dict:
            print(int(dict[num] * num))
            break
        else:
            dict[total - num] = num


              



