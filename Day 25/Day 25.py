if __name__ == "__main__" :   
    l = open("input.txt").readlines()
    # Find public keys
    publicKeys = []   
    subj = 7
    div = 20201227
    for i in range(2):
        n = 0
        value = 1
        key = int(l[i])
        while value != key:
            n+=1
            value = (value * subj) % div         
        publicKeys.append([n,value])    
    
    # Find encryption keys
    encryptionKeys = [] 
    subj = [publicKeys[0][1], publicKeys[1][1]]
    size = [publicKeys[1][0], publicKeys[0][0]]
    for i in range(2):
        value = 1
        for j in range(size[i]):
            value = (value * subj[i]) % div
        encryptionKeys.append(value)
    
    print(encryptionKeys)