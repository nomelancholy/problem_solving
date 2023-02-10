from collections import defaultdict

def solution(lines):
    answer = 0
    
    line_dict = defaultdict(int)
    

    for line in lines:
        for i in range(line[0], line[1]):
            line_dict[i] += 1
    
    answer = len([index for index, count in line_dict.items() if count > 1])
    
    return answer