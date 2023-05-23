def solution(ineq, eq, n, m):
    answer = 0
    
    formula = str(n) + ineq 
    
    if eq != '!':
        formula += eq
        
    formula += str(m)
    
    if eval(formula):
        answer = 1
    
    return answer