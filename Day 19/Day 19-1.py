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
    
    # Find regular expression for rule zero
    match = '^' + Find(rules,rules['0']) + '$'
    
    # Find the number of messages which match the rule
    valid = 0
    for message in messages:
        if re.match(match,message):
            valid += 1
            
    print(valid)