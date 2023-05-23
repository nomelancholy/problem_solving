import re

def solution(myStr):
    
    replaceStr = re.sub('(a|b|c)', '-', myStr)
    
    answer = [ele for ele in replaceStr.split('-') if ele != '']
    
    if len(answer) == 0:
        answer = ['EMPTY']
    
    return answer