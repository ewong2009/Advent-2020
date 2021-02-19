import re
# Solves equation using given rules
def Solve(equation):
    while '(' in equation:
        x = re.search('\([^(^)]*\)',equation).group().replace('(','').replace(')','') 
        equation = equation.replace('(' + x + ')', Evaluate(x))
    return eval(Evaluate(equation))

# Returns equation after evaluating all of the additions first
def Evaluate(equation):
    while '+' in equation:    
        x = re.search('[0-9]+ \+ [0-9]+',equation).group()
        equation = equation.replace(x,str(eval(x)),1)  
    return str(eval(equation))

if __name__ == "__main__" : 
    # Input parsing
    equations = [x.strip() for x in open("input.txt").readlines()]  
    total = 0
    print(Solve(equations[0]), Solve(equations[1]))
    for equation in equations:
        total += int(Solve(equation))
    print(total)