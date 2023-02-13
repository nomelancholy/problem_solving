from collections import defaultdict

def solution(X, Y):
    answer = ''
    x_dict = defaultdict(int)
    y_dict = defaultdict(int)
    
    for c in X:
        x_dict[c] += 1
        
    for c in Y:
        y_dict[c] += 1
        
    commons = set(x_dict.keys()) & set(y_dict.keys())
        
    if len(commons) == 0:
        answer = '-1'
    else:
        for i in range(9, -1, -1):
            if str(i) in commons:
                count = min(x_dict[str(i)], y_dict[str(i)])
                answer += str(i) * count
        if answer.count('0') == len(answer):
            answer = '0'
    
    return answer