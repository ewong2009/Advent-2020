import re
# Returns the evaluation of an equation with brackets
def Solve(equation):
    while '(' in equation:
        x = re.search('\([^(^)]*\)',equation).group().replace('(','').replace(')','') 
        equation = equation.replace('(' + x + ')', Evaluate(x))
    return Evaluate(equation)

# Returns the evaluation of an equation without brackets from left to right
def Evaluate(equation):
    equation = equation.split()
    while len(equation)>1:
        equation = [str(eval(''.join(equation[0:3])))] + equation[3:]
    return str(equation[0])

if __name__ == "__main__" :  
    # Input parsing
    equations = [x.strip() for x in open("input.txt").readlines()]  
    total = 0

    for equation in equations:
        total += int(Solve(equation))
    print(total)