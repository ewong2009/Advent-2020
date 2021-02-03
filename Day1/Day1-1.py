if __name__ == "__main__":
    #Input parsing
    l = open("input.txt","r").readlines()
    
    # Use dictionary to store the compliment of each number
    dict = {}
    total = 2020
    for i in range(len(l)):
        num = int(l[i])
        if int(l[i]) in dict:
            print(int(dict[num] * num))
            break
        else:
            dict[2020 - num] = num


              



