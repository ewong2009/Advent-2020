import re
# Returns regular expression representing rule r
def Find(rules, r):
    string = ''
    # Base case, add a or b
    if r[0] in 'ab':
        string += r[0]
    # Case for two options
    elif '|' in r:
        idx = r.index('|')
        string += '('
        for i in range(idx):
            string += Find(rules, rules[r[i]])
        string += '|'
        for i in range(idx+1,len(r)):
            string += Find(rules, rules[r[i]])
        string += ')'
    # Case for one option
    else:
        for i in r:
            string += Find(rules,rules[i])

    return string

if __name__ == "__main__" :   
    # Input Parsing
    a, b = open("input.txt").read().split("\n\n")
    rstring = a.split('\n')
    messages = b.split('\n')    
    rules = {}
    for item in rstring:
        key, vals = item.replace("\"","").strip().split(": ")
        rules[key] = [i for i in vals.split()]
    
    # Find regular expression for rules 42 and 31
    match42 = Find(rules,rules['42'])
    match31 = Find(rules,rules['31'])
    # Now we can create a regular expression for rule zero
    match = "^(" + match42 + ")+" +  "(" + match31 + ")+$"

    # Find the length of a string which matches each rule
    len42 = len(re.search(match42,messages[0]).group(0))
    len31 = len(re.search(match31,messages[0]).group(0))
    
    # Find if the message matches rule zero
    # If it does find the number of matches to each rule within the message
    valid = 0
    for message in messages:
        if re.match(match,message):
            count42 = 0
            messageLen = len(message)
            n = int(messageLen/len42)
            # Find matches for rule 42
            for i in range(n):
                if not re.match(match42,message[i*len42:i*len42+len42]):
                    break
                count42 += 1
            count31 = (messageLen - count42*len42) / len31
            # message is valid only if there are more rule 42 matches than rule 31 matches
            valid += count42 > count31            

    print(valid)
