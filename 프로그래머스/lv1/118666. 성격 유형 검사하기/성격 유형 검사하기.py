from collections import defaultdict

def solution(survey, choices):
    answer = ''
    
    types = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    
    typedict = defaultdict(int)
    
    for c_type in types:
        typedict[c_type]
        
    for index, choice in enumerate(choices):
        test_kind = survey[index]
        if choice > 4:
            typedict[test_kind[1]] += choice - 4
        elif choice < 4:
            typedict[test_kind[0]] += 4 - choice
    
    for i in range(0, len(types), 2):
        if typedict[types[i]] < typedict[types[i + 1]]:
            answer += types[i + 1]
        else:
            answer += types[i]
    
    return answer